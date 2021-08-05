
Project Title:  **Cab Price Prediction**

The project uses a model of random forest regression to predict the estimated cab fare, using inputs like:

        - Distance
        - Cab Company 
        - Cab Service
        - Source Location
        - Destination Location
        - Surge Multiplier
        - Temperature [Source & Destination]
        - Cloudiness [Source & Destination]
        - Rainfall [Source & Destination]
        


[app.py](../main/app.py) is the application file which makes use of the model created using the [lyft-uber-price-prediction.ipynb](../main/lyft-uber-price-prediction.ipynb) notebook

[app(Using IBM Cloud).py](https://github.com/smartinternz02/SI-GuidedProject-4931-1627533314/blob/main/app(Using%20IBM%20Cloud).py) on the other hand uses a model deployed on IBM Cloud, created using the [lyft-uber-price-prediction (IBM Watson Version)](https://github.com/smartinternz02/SI-GuidedProject-4931-1627533314/blob/main/lyft-uber-price-prediction%20(IBM%20Watson%20Version)) notebook, to perform the same prediction.

