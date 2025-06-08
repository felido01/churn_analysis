# Customer Churn Analysis Dashboard: Stakeholder Report

## Overview

The **Customer Churn Analysis Dashboard** is an easy-to-use, web-based tool that helps telecom companies keep more customers by understanding why they leave and spotting those at risk. It uses customer data to provide clear insights, attractive charts, and predictions to guide smarter retention plans. Hosted online, the dashboard is ready for your team to explore and use right away.

**Why It Matters**:
- Shows what’s driving customers to leave, like short-term contracts or high bills.
- Predicts which customers might leave, so you can act early.
- Could save significant revenue by keeping more customers (e.g., $120,000 a year for 10,000 customers).
- Try it live at: [https://appb-3hmyvaxpwn2jzkevjprasz.streamlit.app/](https://appb-3hmyvaxpwn2jzkevjprasz.streamlit.app/).

**Created by**: Felix Idowu  
**Website**: [https://felido01.github.io/felixidowu01/intro.html](https://felido01.github.io/felixidowu01/intro.html)  
**Version**: 1.0.0  
**Date**: June 8, 2025  

---

## Why We Built This

Losing customers is a big challenge for telecom companies, costing money and growth opportunities. This dashboard helps by:
- Showing who’s leaving and why, based on their services, bills, or personal details.
- Predicting which customers are likely to leave, so you can reach out with offers or support.
- Making data easy to understand with charts and reports anyone can use.
- Helping your team make better decisions to keep customers happy and loyal.

This tool is for telecom leaders who want to save money, improve customer relationships, and stay ahead of competitors.

---

## What We Learned

While building and testing the dashboard with sample telecom data, we found key insights that can help your business:

### 1. **What’s Causing Customers to Leave**
- **Churn Rate**: About 26% of customers in the sample data left, showing a real need to act.
- **Big Factors**:
  - **Short Contracts**: Customers on month-to-month plans are much more likely to leave (40% churn) than those on two-year plans (5% churn).
  - **Internet Type**: Customers with fiber optic internet leave more often (30% churn), possibly due to high costs or service issues.
  - **New and Expensive Plans**: Customers who’ve been with the company less than a year and pay over $70 a month are at higher risk.
- **Customer Types**: Older customers or those without families tend to leave slightly more often.

**What This Means**: You can focus on offering longer contracts or fixing fiber optic service to keep more customers.

### 2. **Predicting Who Might Leave**
- **How It Works**: The dashboard uses two smart tools to predict churn:
  - **RandomForest**: Gets about 80% of predictions right, spotting patterns like contract length or bill size.
  - **LogisticRegression**: Slightly less accurate (78%) but quick and simple.
- **Key Clues**: Short time with the company, high monthly bills, and short contracts are the biggest signs a customer might leave.
- **Personal Predictions**: You can enter a customer’s details to see their risk of leaving (e.g., 65% chance for someone on a pricey, short-term plan).

**What This Means**: You can reach out to risky customers with special offers or support to keep them.

### 3. **Easy for Everyone to Use**
- **Simple Design**: The dashboard has clear charts (like pie charts or graphs) and filters to focus on specific customers, like those with short contracts.
- **Quick Options**: Buttons like “High-Risk Customers” make it fast to find important groups.
- **Shareable Results**: Download data or reports to share with your team or use in meetings.
- **Online Access**: Check it out anytime at [https://appb-3hmyvaxpwn2jzkevjprasz.streamlit.app/](https://appb-3hmyvaxpwn2jzkevjprasz.streamlit.app/).

**What This Means**: Your marketing, sales, or support teams can use this without needing data experts.

### 4. **Ready to Grow**
- **Handles Data Well**: Works smoothly even if some data is missing or messy, making it reliable.
- **Fast Performance**: Can manage thousands of customer records and could handle more with tweaks.
- **Online Hosting**: Already live on a cloud platform, so your team can access it from anywhere.

**What This Means**: The tool is good to go but can be tailored or expanded for bigger needs.

### 5. **Things to Keep in Mind**
- **Data Needs**: The tool expects a specific customer data file with details like contracts and bills. Without it, some features won’t work.
- **Prediction Limits**: Predictions are based on the sample data and might need updates for your specific customers.
- **Security**: The online version doesn’t have logins yet, so sensitive data needs extra protection.

**What This Means**: Check your data fits the tool’s needs and plan for security if you use it widely.

---

## How This Helps Your Business

The Customer Churn Analysis Dashboard can make a real difference by tackling customer loss:

- **Save Money**: Cutting churn by 5-10% could save $120,000 a year for a 10,000-customer company with $100 average monthly bills.
- **Smarter Marketing**: Focus on risky customers, like those on short contracts, to get better results from your budget.
- **Save Time**: Quick insights and predictions mean less time crunching numbers and more time acting.
- **Happier Customers**: Reaching out early with offers or support builds trust and loyalty.
- **Stay Ahead**: Using data to keep customers gives you an edge over competitors who react too late.

**See It in Action**: Visit [https://appb-3hmyvaxpwn2jzkevjprasz.streamlit.app/](https://appb-3hmyvaxpwn2jzkevjprasz.streamlit.app/) to try it yourself.

---

## What You Should Do Next

Here’s how to make the most of the dashboard:

1. **Start Using It Now**:
   - Visit the live tool at [https://appb-3hmyvaxpwn2jzkevjprasz.streamlit.app/](https://appb-3hmyvaxpwn2jzkevjprasz.streamlit.app/).
   - Make sure your customer data includes details like contracts and bills.
   - **To Do**: Spend 1-2 days training your team to use the dashboard.

2. **Make It Your Own**:
   - Add the ability to upload your own data files for more flexibility.
   - Connect it to your customer system (like Salesforce) for automatic updates.
   - Include fancier charts or smarter prediction tools if needed.
   - **To Do**: Plan 2-4 weeks to customize it for your business.

3. **Keep Data Safe and Scale Up**:
   - Add logins to protect customer information.
   - Move to a bigger, secure online platform if lots of people need to use it.
   - **To Do**: Work with your IT team for 1-2 weeks to set this up.

4. **Act on What You Learn**:
   - Offer better deals to customers on short contracts.
   - Improve fiber optic service to keep those customers happy.
   - Use predictions to call or email at-risk customers with special offers.
   - **To Do**: Get marketing and support teams working on this in 1-2 months.

5. **Check Results and Improve**:
   - See if fewer customers are leaving and how much money you’re saving.
   - Ask your team what they like or want to change in the tool.
   - **To Do**: Review progress every 3 months to make it even better.

---

## Possible Concerns and Solutions

| **Concern** | **What It Means** | **How to Fix It** |
|-------------|-------------------|-------------------|
| **Wrong Data** | Your data might not match what the tool needs. | Check your data has the right details; fix any issues before starting. |
| **Team Not Ready** | Staff might not know how to use the dashboard. | Offer quick training and simple guides to get them started. |
| **Predictions Off** | Predictions might not work perfectly for your customers. | Update the tool with your data regularly to keep it accurate. |
| **Data Safety** | Customer info could be at risk online. | Add logins and use a secure platform to keep data safe. |

---

## Getting Started

To make this dashboard work for your business:
- **Right Away (1-2 Weeks)**:
  - Try the live tool: [https://appb-3hmyvaxpwn2jzkevjprasz.streamlit.app/](https://appb-3hmyvaxpwn2jzkevjprasz.streamlit.app/).
  - Check your data and test the dashboard with your team.
  - Set up a short demo to see how it works.
- **Next 1-2 Months**:
  - Train your team and start using insights to keep customers.
  - Plan how to customize or secure the tool.
- **Over 3-6 Months**:
  - Connect it to your systems and make it bigger if needed.
  - Track how much you’re saving and make the tool even better.

---

## Get in Touch

If you have questions, want to customize the tool, or need help:
- **Email**: [felixidowu.01@gmail.com](mailto:felixidowu.01@gmail.com)
- **LinkedIn**: [Felix Idowu](https://www.linkedin.com/in/felix-idowu-4347a4268/)
- **GitHub**: [felido01](https://github.com/felido01)
- **Creator**: Felix Idowu
- **Website**: [https://felido01.github.io/felixidowu01/intro.html](https://felido01.github.io/felixidowu01/intro.html)

---

## Final Thoughts

The Customer Churn Analysis Dashboard is a game-changer for telecom companies, helping you keep more customers, save money, and build stronger relationships. It’s easy to use, packed with useful insights, and ready to go online. By starting with this tool, you can make smarter decisions and stay ahead in a tough market.

**Take the First Step**: Visit [https://appb-3hmyvaxpwn2jzkevjprasz.streamlit.app/](https://appb-3hmyvaxpwn2jzkevjprasz.streamlit.app/) today to see how it can help your business keep customers and grow.

---

**Created by Felix Idowu** | [Visit My Website](https://felido01.github.io/felixidowu01/intro.html)
