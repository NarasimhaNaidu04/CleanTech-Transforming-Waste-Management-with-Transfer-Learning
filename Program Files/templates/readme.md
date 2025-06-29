#project executable files 

Project files consists of app.py (backend ) and index.html (frontend) :

🧠 app.py – Backend Logic (Flask App)

The app.py file serves as the main backend application built with Flask. It handles routing, image upload, and prediction logic. When a user uploads an image through the web interface, app.py:

Receives the uploaded file via a POST request.
Saves the image in the static/uploads/ directory.
Preprocesses the image (resizing, normalization, etc.).
Passes it through a pre-trained VGG16 model (vgglo.hs) to predict the waste category.
Returns the prediction result (biodegradable, recyclable, or trash) to be displayed on the frontend.

This file integrates TensorFlow/Keras for the model and uses standard Flask functions to handle image serving and user interaction.

🌐 index.html – Frontend Interface

The index.html file is located in the templates/ folder and acts as the main user interface of the application. It allows users to:

Upload an image of waste using a file input field.
Submit the image to the backend via a form.
View the uploaded image and classification result (rendered dynamically after the prediction).

The page is styled using basic HTML and CSS (optional style.css in static/), and designed to be simple, intuitive, and accessible for users to test the waste classification in real time.
