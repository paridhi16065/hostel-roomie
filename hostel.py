from flask import Flask,render_template,request,redirect

app = Flask(__name__)

l = ""
@app.route('/',methods=['GET'])
def handle_root():
	return render_template('form.html')
	

@app.route('/responses',methods=['POST'])
def handle_data():
	file1=open("lists.txt","a")
	global l
	l=''
	l+=request.form["roll_number"]+","
	l+=request.form["rad1"]
	l+=request.form["rad2"]
	l+=request.form["rad5"]
	l+=request.form["rad4"]         #questions arranged in order of priority
	l+=request.form["rad3"]
	file1.write(l)
	file1.write('\n')
	file1.close()
	return redirect("http://localhost:8000/answer")

@app.route('/answer',methods=['GET'])
def handle_root1():
	diff=30000
	file1=open("lists.txt","r")
	# print file1.readlines()[0].split(',')[1]
	lines = file1.readlines()
	print lines
	a=int(lines[-1].split(',')[1])
	print a
	l=lines[0]
	for line in lines[0:-2]:
		b=int(line.split(',')[1])
		print b
		if abs(b-a)<diff:
			if abs(b-a)!=0:
				diff=abs(b-a)
				l=line
	rn=l.split(',')[0]
	file1.close()
	return"""<html>
			<head> </head>
			<body><H1>Your Suitable Roommate is: """+str(rn) +"""</h1> </body> </html> """


app.run(debug=True, port=8000)