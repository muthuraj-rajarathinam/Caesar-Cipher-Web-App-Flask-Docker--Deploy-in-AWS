## 🔐 Caesar Cipher Web App — Flask + Docker + AWS

This project demonstrates modern cloud-native deployment practices by containerizing a Python Flask web application with Docker and deploying it to AWS. The application itself is a Caesar Cipher tool, allowing users to encrypt or decrypt text with a customizable shift, but the primary focus is on the containerization and cloud deployment workflow.

By packaging the app as a Docker container, we ensure that it runs identically across any environment—locally, on-premises, or in the cloud. This approach eliminates "it works on my machine" issues and simplifies scaling, updating, and maintaining the application.

The project is designed for rapid deployment to AWS using services such as Amazon ECS (Elastic Container Service), AWS Elastic Beanstalk, or AWS App Runner. You can build and test the container locally, then push the image to a container registry (like Amazon ECR), and deploy it to AWS for high availability, scalability, and integrated monitoring

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

