from flask import Flask,render_template,request
import numpy as np
from skimage.feature import greycomatrix
headings = (1,2,3,4,5)
heading1 = (0,1,2,3,4,5,6,7,8)
image = np.array([[1, 1, 5, 6, 8],
                  [2, 3, 5, 7, 1], 
                  [4, 5, 7, 1, 2],
                  [8, 5, 1, 2, 5]])
#x= print(result[:, :, 0, 0])
application = Flask(__name__) 

@application.route("/", methods =['POST','GET'])
def dataFrom():
   if request.method == "POST":
      d = request.form["distance"] 
      a= request.form["angle"]
      print(d,a)
      result = greycomatrix(image, [d], [a], levels=9)
      return render_template('formdata.html',headings= headings,heading1= heading1,image=image,result=result) 

   else:
      return render_template('dataFrom.html',image=image) 

if __name__ == '__main__':
   application.debug = True
   application.run() 
