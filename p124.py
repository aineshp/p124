from flask import Flask,jsonify,request
app=Flask(__name__)
data=[{'id':1,
        'Contact':u'9987644456',
        'Name':u'Raju',
        'done':False},
        {'id':2,
        'Contact':u'9876543222',
        'Name':u'Rahul',
        'done':False}]
@app.route('/add_Details',methods=['POST'])
def addDetails():
    if not(request.json):
        return jsonify({
            'status':'error',
            'message':'Please provide the data'
        },400)
    details={'id':data[-1]['id']+1,
            'Contact':request.json['Contact'],
            'Name':request.json.get('Name',''),
            'done':False}
    data.append(details)
@app.route('/get_details')
def get_details():
    return jsonify({
        'data':data
    })    
if(__name__=='__main__'):
    app.run(debug=True) 
    

