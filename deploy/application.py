from flask import Flask, render_template, request, jsonify
application = app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://sparta:test@cluster0.r6mbvxn.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
   return render_template('index.html')

@app.route("/guestbook", methods=["POST"])
def guestbook_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']
    
    doc = {
        'name':name_receive,
        'comment':comment_receive
    }
    db.fans.insert_one(doc)
    return jsonify({'msg': '등록 완료.'})

@app.route("/guestbook", methods=["GET"])
def guestbook_get():
    all_comments = list(db.fans.find({},{'_id':False}))
    return jsonify({'result': all_comments})

@app.route("/guestbook/delete", methods=["DELETE"])
def guestbook_delete():
    name_receive = request.form['name_give']
    db.fans.delete_one({'name':name_receive})
    return jsonify({'msg': '잉.. 지우지 말지..'})

if __name__ == '__main__':
    app.run()