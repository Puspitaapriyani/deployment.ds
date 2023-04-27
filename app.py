'''
	Contoh Deloyment untuk Domain Data Science (DS)
	Orbit Future Academy - AI Mastery - KM Batch 3
	Tim Deployment
	2022
'''

# =[Modules dan Packages]========================

from flask import Flask,render_template

# =[Variabel Global]=============================

app   = Flask(__name__)

# =[Routing]=====================================

# [Routing untuk Halaman Utama atau Home]	
@app.route("/")
def beranda():
    return render_template('index.html')

# =[Main]========================================

if __name__ == '__main__':
	
	# Run Flask di localhost 
	app.run(host="localhost", port=5000, debug=True)
	
	


