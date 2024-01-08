
# Store Project

This project consists of stores and items in the market. The constituent part of a single store and single item is shown below. Each store has a store id assigned to it and the same for an item.


For backend, activate the virtual environment, build and run through the code given below.


## Compile & Run



```bash
source flask2/bin/activate

```

```bash
sudo docker build -t rest-api .

```

```bash
sudo docker run -p 5000:5000 rest-api

```




## Usage/Examples

```python
items = {67ddd636b0ed42a0adc8c7881d16c28d : "Name" : :Chair",
                                             "Price" : 17.99,
                                             "item id" : 67ddd636b0ed42a0adc8c7881d16c28d
                                             };


store = {9805c262c62b4643becc07dc51f84a51 : {"id": "9805c262c62b4643becc07dc51f84a51",
   					     "name": "My Store2"
  				             },
```


## Screenshots
(If screenshot is not availabe, click on the link)

All items and stores

![Screenshot from 2024-01-08 14-42-34](https://github.com/rkirtii/Store-Project/assets/142138548/493d69ce-683a-47b6-a60b-7bf57f4573b4)

Empty stores and items

![Screenshot from 2024-01-08 14-52-35](https://github.com/rkirtii/Store-Project/assets/142138548/ce0e5c05-ece2-40d8-842d-5e3f09490b75)
![Screenshot from 2024-01-08 14-52-32](https://github.com/rkirtii/Store-Project/assets/142138548/34313914-b784-4098-ba6f-996e62d2f911)



Fetching all stores
![a5f8cae9-612b-4af7-81db-7da0fa5348e7](https://github.com/rkirtii/Store-Project/assets/142138548/a504f6bc-8f8a-4f08-a13b-f45019627667)


Deleting Mystore2
![fb79aa59-e205-403a-b57f-2b94e2af73e2](https://github.com/rkirtii/Store-Project/assets/142138548/0a30f733-3b27-415c-834a-da0a2a24f192)


Fetching all items
![27b4d9a6-1962-4dee-874b-1221b2d17f2b](https://github.com/rkirtii/Store-Project/assets/142138548/5bf82122-b5f2-486e-8e3c-a680ab166ff9)
