# :robot: FraudDetection :car:

## :arrow_forward: Introduction
Bank transactions represent an important step for the automation paying industry. Oftentimes, these can be fraudulent, leading to losing a great amount of money. This project tries to identify those transactions and display a map showing them

## :memo: Description

Consistency represents the key factor that reveals the fraudulent attempts. The project implements self-organized maps imported from pypi.org that detect unexpected details among transactions. Displaying the map of organized data, it becomes obvious if a transaction is fraudulent or not.
## :computer: Implementation

The dataset is composed of multiple rows associated with information for every transaction. Features are then transformed by MinMaxScaler and passed to the model. Hyperparameters are chosen to best visualize possible bank frauds. Index.html represents the default page that will appear when the application is stated.


## :exclamation: Instructions
The application can be stated by using 'python manage.py runserver' command inside BankFraud/BankFraud folder

  
 ## :camera: Graph
<p align="center">
 <img src="https://github.com/Marius2504/FraudDetection/blob/master/map.png" width="600">
</p>

