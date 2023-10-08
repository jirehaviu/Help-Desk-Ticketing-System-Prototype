# Help-Desk Ticketing System Prototype
**Author**: Jireh Tearea  
**ID**: 20230851  
**Educational Institution**: Whitecliffe  
**Subject**: IT5016 Software Development  
**Assignment 2**: Software Project  
**Assignment 3**: Research Repository  


## Table of Contents
* [Introduction](#introduction)
* [Features](#features)
* [Technologies](#technologies)
* [Setup](#setup)
* [Instructions](#instructions)

## Introduction
This software prototype is my submission for IT5016 Software Development, Assignment 2: Your Software Project & Assignment 3: Reasearch Repository. This software that I've developed is a help-desk ticketing system for support staff and administrator use only.

## Features
**Login Screen**  
-**Authenticator**, The Help-Desk or IT Department Staff members need to input their username and password in order to gain access to their option screen, ensuring proper access control.

**Help Desk Department Option Screen**  
-**Create Ticket**, Users have the ability to create and submit a new support ticket for the IT Department to analyze.  
-**View Tickets**, With this option, the users can retrieve all created tickets for reference or review.  
-**Respond To Ticket**, Once the admins have resolved a particular ticket, users can provide additional feedback.  
-**Logout**, After the user has finished their task using this software, they can choose to log out from the software.  

**IT Department Option Screen**  
-**View Tickets**, Admins have the ability to gather the required information on all tickets for analysis and tracking purposes.  
-**Resolve Ticket**, This option allows administrators to respond to a submitted ticket and resolve the issue that coincides with the ticket. If a support staff requests a password, the admin can initiate an automatic generated password.  
-**Change Admin Password**, Administrators have the ability to change/alter their or another admins password.
-**Ticket Statistics**, This option retreives statistices based on ticket total, opened tickets, closed tickets.  
-**Reopen Ticket**, When a certain ticket is completed (*closed), Administrators have the access to reopen a particular ticket.  
-**Logout**, After the adminisrator has finished their task using this software, they can choose to log out from the software. 

## Technologies
This software is developed using:

[**Visual Studio Code**](https://code.visualstudio.com/download#) `version: 1.82.3`  
[**Python**](https://www.python.org/downloads/release/python-3110/) `version: 3.11.0`  
[**Python Library**](https://docs.python.org/3/library/shutil.html) `module: shutil`  

## Setup  
In order to begin working on this software, it is necessary to set up your development environment, which includes installing the widely used code editor, Visual Studio Code, as well as Python, which is utilized in this software.  
  

**Step 1: Installing Python**
1. **Download Python:**
   Visit the official [Python website](https://www.python.org/downloads/release/python-3110/) and download this version or later for your specific operating system - Windows, macOS or Linux.
2. **Install Python:**
   Proceed with the installation by running the previously downloaded installer. Before proceeding, ensure that you check the box labeled "Add Python to PATH" for the installation.
3. **Verify Installation:**
   To execute the following command, open a command prompt on Windows or a terminal on macOS and Linux
   `python --version`
   The Python version should be displayed.
     
**Step 2: Installing Visual Studio Code**  
1. **Download Visual Studio Code:**  
   Visit the official [Visual Studio Code website](https://code.visualstudio.com/download#) and download the installer for your specific operating system - Windows, macOS, or Linux.  
2. **Install Visual Studio Code:**  
   Please follow the installation instructions that are provided on the website for your particular operating system.
3. **Open Visual Studio Code:**  
   After successfully installing Visual Studio Code, you can launch the application.

 **Step 3: Accessing Software Files in Visual Studio Code**  
1. To open Visual Studio Code, click on the application icon.  
2. To open a folder:  
    *1.* Click on the "File" menu located in the top-left corner.  
    *2.* If you are working with a workspace, select "Add Folder to Workspace". If you are not using a workspace, select "Open Folder...".    
    *3.* Browse to the location of the downloaded software folder and click "Open". Alternatively, you can also drag and drop your project folder directly into the Visual Studio Code window.
3. After opening the folder, you will find a file explorer on the left sidebar. This allows you to navigate through the files.    
4. To access the `Help-Desk-Ticketing-System-Prototype` software in the terminal:  
   *1.* To begin using the software, double click on `main.py` file in the file explorer.
5. Run python file:  
   To run the software, click on the terminal icon in the top-right corner `run python file`.

## Instructions
Before you start using this software, please make sure to take note of the following default usernames and passwords provided below.  
These crentials are intended for Help-Desk Staff & IT Department, and they will allow you to explore and understand how the software operates:  

**Help-Desk Staff 1:**   
* Username: `help_desk_user1`  
* Password: `password1`  

**Help-Desk Staff 2:**   
* Username: `help_desk_user2`  
* Password: `password2`  

**Help-Desk Staff 3:**   
* Username: `help_desk_user3`  
* Password: `password3`  

**IT Department Staff 1:**   
* Username: `admin1`  
* Password: `password1`  

**IT Department Staff 2:**   
* Username: `admin2`  
* Password: `password2`  

**IT Department Staff 3:**   
* Username: `admin3`  
* Password: `password3`

Feel free to use these credentials to log in and experience the software firsthand.  

  
**Step 1: Accessing the Project Files**

Follow the steps below to download and access the necessary `Help-Desk-Ticketing-System-Prototype` files for this project:

1.  Download the following Python files:

    *   `main.py`
    *   `class_ticket.py`
    *   `class_helpdesk.py`
    *   `class_admin.py`

2.  Open Visual Studio Code.
3.  Navigate to the folder where you saved the downloaded Python files.
4.  To do this, follow the instructions provided [here](#setup).

Once you have completed these steps, you'll be ready to start useing `Help-Desk-Ticketing-System-Prototype` files in Visual Studio Code.

**Step 2: Running the Software**  

1.  In Visual Studio Code, follow the instructions on **Step 3: Accessing Software Files in Visual Studio Code** [here](#setup) to run the software.

**Step 3: Department Option Screen**  
1. When the program launches, you will be presented with a login selection screen. Type the option number that corresponds to that option.
  
  
   ```  
   1 - Help Desk Department     
   2 - IT Department      
   3 - Neither
   ```        
When you have selected your preferred option press enter.

3. Depending on the department you have chosen, you will be prompt to input your username and password before proceeding further.  
   *Please note that the username and passwords are already provided for you to access either departments, if you wish to alter or change those credtials you can do that by changing the instances in the `class_admin.py` file.*

**Step 4 - Part 1: Help-Desk Option Screen**  
Once you have proceed through option 1: `1 - Help Desk Department`, you are presented with a set of options assigned to Help-Desk Support Staff. Below are the following:  

`1 - Create Ticket`:   
To create a new support ticket, follow the steps below:  

1.  Provide the necessary information related to the issue you are experiencing. This may include details such as the description of the problem and any error messages.    
2.  Additionally, provide your credentials or any other required identification information.   
3.  Once you have provided all the required information, submit the ticket.    
4.  Upon successful submission, you will receive a Ticket ID Number. It will be displayed on the screen in the following format:  

        Ticket Submitted SuccessfullyYour Ticket ID Number is 2004  
  
    Take note of this Ticket ID Number for future reference.  
  
`2 - View Tickets`:  
You will be provided all information on every created ticket for referencing or response from the IT department.    

`3 - Respond to Ticket`:    
You will be prompted to input your desired ticket id number. You will also be prompted to type your response, looking like this:    
  
 ```
  Enter Ticket ID Number: 2001
     Enter Reply: Thank you for assitance
 ```
  
`4 - Logout`:  
Once you have completed you tasks, you have the ability to logout. 

**Step 4 - Part 2: IT Department Option Screen**  
Once you have proceed through option 2: `2 - IT Department`, you are presented with a set of options assigned to IT Department. Below are the following:  

`1 - View Tickets`:  
You will presented with a set of nessary ticket information. The information displayed will look similar to this below:  

```  
Ticket ID: 2002    
Status: Closed    
Description: Hardware component faulty    
```  
  
This will keep track on what ticket needs to be resolved, reopened or for report perposes.  

`2 - Resolve Ticket`:  
To resolve a ticket and update its status to 'Closed', follow the steps below:  
  
1.  Locate the ticket you want to resolve and take note of its unique identification number. This number is referred to as the 'opened' ticket ID.  
2.  Provide the 'opened' ticket ID number as input when prompted.  
3.  Enter the updated resolve response for the ticket when prompted.  
4.  Once entered, the response will be saved, and the ticket's status will be updated to `Status: Closed`. If the description displays `password change` a new password will be automatically generated.    

`3 - Change Admin Password`:  
To reset an administrator's password, follow the steps below:

You will be prompted to enter the username of the administrator whose password needs to be reset. If you are resetting your own password, enter your own username. Otherwise, enter the username of the respective administrator.

1.After entering the username, you will be asked to enter a new password for the administrator.
2.When prompted, enter the new password.
3.Once entered, the system will generate and set the new password for the administrator.
  
```    
Enter Admin Username: admin3
Enter new password: password****
```    
  
`4 - Ticket Statistics`:  
This will generate the current stats of all tickets generated, example below:
  
```      
Number of Tickets Submitted: 3  
Number of Tickets Completed: 1  
Number of Tickets Open: 2  
```  

`5 - Reopen Ticket`:   
You will have the abiltiy to reopen a ticket that is currently `Status: Closed` to `Status: Open`  
  
`6 - Logout`:  
Once you have completed you tasks, you have the ability to logout. 
   

