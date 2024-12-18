Restaurant Complaint Classification and Response System
Deployment Link : 
https://restaurant-complaint-classification-and-response-system-jecyt4.streamlit.app/

Project Explanation

Introduction: The Restaurant Complaint Classification Project aims to improve customer service in the restaurant industry by automating complaint management. It leverages natural language processing (NLP) techniques to classify complaints, generate automated responses, and provide valuable insights to restaurant owners.

User Roles:

Customers: They can submit complaints and receive instant auto-responses based on the nature of their complaint.

Restaurant Owners: They can analyze complaints over selected periods (e.g., last 30, 60, or 90 days) to identify trends and areas for improvement.

Key Features:

Complaint Submission and Response:

Customers submit their complaints through an interface.
The system categorizes the complaint based on predefined categories (e.g., service, food quality) and assesses severity and urgency.
A custom function generates automated responses tailored to the complaint's characteristics.

Complaint Analysis for Owners:

Owners can select a review period to view the count and distribution of complaints across categories.
The system provides insights into complaint severity, urgency, and whether the complaint is first-time or repeated.

Technical Approach:

Data Collection: Utilized web scraping techniques to gather negative reviews specifically from Absolute Barbeques, enriching the dataset for analysis.

Multi-Label Classification with BERT: Fine-tuned a BERT model to classify complaints into multiple categories based on the text input.

Sentiment Analysis: Used sentiment analysis to classify complaints by urgency and severity.

Streamlit Dashboard: Developed an interactive web app using Streamlit, allowing customers and owners to interact with the system seamlessly.

Outcomes:

Enhanced customer satisfaction through quick, personalized responses to complaints.
Provided restaurant owners with actionable insights to improve service quality and address recurring issues effectively.

