## 🔐 Caesar Cipher Web App — Flask + Docker + AWS

This is a simple and interactive **Caesar Cipher Web Application** built using Python and Flask. It allows users to enter any text and either encrypt or decrypt it by applying the Caesar cipher technique with a customizable shift amount. The entire processing is done in memory without relying on any external APIs, databases, or file storage, making it lightweight and easy to deploy.

The app features a modern, eye-catching user interface styled with Bootstrap 5, providing a clean and responsive experience on both desktop and mobile devices.

This project is containerized using Docker, enabling consistent deployment across different environments. It can be easily deployed to cloud platforms such as AWS using services like Elastic Beanstalk or App Runner.

---

### 📘 Table of Contents

* [📌 Project Description](#-project-description)
* [🚀 Features](#-features)
* [📂 Project Structure](#-project-structure)
* [🧪 Caesar Cipher Logic](#-caesar-cipher-logic)
* [🛠️ Local Development](#️-local-development)
* [🐳 Docker Setup](#-docker-setup)
* [☁️ AWS Deployment Guide](#️-aws-deployment-guide)
* [📚 Technologies Used](#-technologies-used)
* [✍️ Author](#️-author)
* [📄 License](#-license)

---

## 📌 Project Description

The **Caesar Cipher** is one of the oldest known encryption techniques. It works by shifting letters in the alphabet by a fixed number of positions.

This app provides a fully interactive web interface to:

* 🔐 Encrypt messages with a shift value
* 🔓 Decrypt messages using the same shift
* 🌐 Access the tool via browser using a Flask backend
* 🐳 Containerize the app using Docker for seamless deployments
* ☁️ Host on AWS Elastic Beanstalk for live access

---

## 🚀 Features

* Web interface for Caesar Cipher encryption and decryption
* Pure Python logic (no external APIs or databases)
* Responsive UI with Bootstrap 5
* Lightweight Docker container support
* Easily deployable to AWS via Elastic Beanstalk

---

## 📂 Project Structure

```
caesar-cipher-app/
├── app.py             # Main Flask app with Caesar Cipher logic
├── Dockerfile         # Docker build instructions
├── requirements.txt   # Python dependencies
```

---

## 🧪 Caesar Cipher Logic

The Caesar Cipher shifts each character by a specified number of positions.

Example:

```
Input:  HELLO
Shift:  3
Output: KHOOR
```

* Supports both encryption and decryption
* Preserves case sensitivity
* Ignores non-alphabetic characters

---

## 🛠️ Local Development

### ✅ Prerequisites

* Python 3.8 or higher
* Docker (optional, for containerization)

### 🔧 Run Without Docker

```bash
pip install -r requirements.txt
python app.py
```

Visit: [http://localhost:5000](http://localhost:5000)

---

## 🐳 Docker Setup (Local)

### Build & Run Docker Container

```bash
# Build the image
docker build -t caesar-cipher-app .

# Run the container
docker run -p 5000:5000 caesar-cipher-app
```

Then visit: [http://localhost:5000](http://localhost:5000)

---

## ☁️ AWS Deployment Guide

### ✅ Prerequisites

* AWS account
* `Dockerfile`, `app.py`, and `requirements.txt` in the root directory
* Zip file containing only these files

---

### 📁 Step 1: Zip the App for Upload

Make sure you’re zipping **the contents**, not the folder:

```bash
zip -r caesar-cipher-app.zip app.py Dockerfile requirements.txt
```

---

### 🌐 Step 2: Deploy via AWS Console

1. Go to [Elastic Beanstalk Console](https://console.aws.amazon.com/elasticbeanstalk)
2. Click **Create Environment**
3. Choose:

   * **Environment Type**: Web server
   * **Platform**: Docker
4. Under **Application Code**:

   * Upload `caesar-cipher-app.zip`

Click **Create Environment**

---

### ⏱️ Step 3: Wait for Deployment

* The environment will take 2–4 minutes to provision
* When status = ✅ **"Health: Green"**, your app is live
* If status is ❌ "Degraded":

  * Go to **Logs > Request Logs > Last 100 Lines** to debug

---

### 🌍 Step 4: Access Your Live App

Your app will be hosted at:

```
http://<your-env>.elasticbeanstalk.com
```

---

### 🧼 Step 5: Clean Up (Stop Billing)

* Go to **Elastic Beanstalk Console**
* Click your environment
* Click **Actions > Terminate Environment**

---

### 📚 Notes

Ensure `app.py` contains:

```python
app.run(host='0.0.0.0', port=5000)
```

And your `Dockerfile` includes:

```dockerfile
EXPOSE 5000
CMD ["python", "app.py"]
```

---

## 📚 Technologies Used

* Python 3
* Flask
* Bootstrap 5
* Docker
* AWS Elastic Beanstalk

---

## ✍️ Author
Muthuraj

## 📄 License

This project is licensed under the **MIT License**. See the `LICENSE` file for more details.

---

Would you like me to generate a `LICENSE` file and `.gitignore` to complete your GitHub repo setup?
