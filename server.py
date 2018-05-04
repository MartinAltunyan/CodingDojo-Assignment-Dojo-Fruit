from flask import Flask, render_template, request, redirect
app = Flask(__name__)
# our index route will handle rendering our form
@app.route('/')
def index():
    return render_template("index.html")
# this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route
@app.route('/result', methods=['POST'])
def getting_info():
    print("Got Post Info")
    # we'll talk about the following two lines after we learn a little more about forms
   
    name = request.form['name']
    studentid=request.form['studentid']
    strawberry=request.form['strawberry']
    raspberry=request.form['raspberry']
    apple=request.form['apple']
    # redirects back to the '/' route

    return render_template('result.html',name=name,studentid=studentid,strawberry=int(strawberry),apple=int(apple),raspberry=int(raspberry),sum=int(raspberry)+int(apple)+int(strawberry))
if __name__=="__main__":
    app.run(debug=True) 

