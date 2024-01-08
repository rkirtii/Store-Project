
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
(If screenshot is not availabe, click on the lick

All items and stores

![Screenshot from 2024-01-08 14-42-34](https://github.com/rkirtii/Pro/assets/142138548/90af41e5-2d5d-4261-9867-226d663e9876)

(https://github-production-user-asset-6210df.s3.amazonaws.com/142138548/294855303-90af41e5-2d5d-4261-9867-226d663e9876.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20240108%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240108T132213Z&X-Amz-Expires=300&X-Amz-Signature=4f22c7e1a2d18b42c28a4dc5cd375afb5370ec12833dede2df8daa93cc2981e1&X-Amz-SignedHeaders=host&actor_id=142138548&key_id=0&repo_id=677940319)

Empty stores and items

![Screenshot from 2024-01-08 14-52-35](https://github.com/rkirtii/Pro/assets/142138548/bb548797-bd09-4234-a49c-07542994def9)
![Screenshot from 2024-01-08 14-52-32](https://github.com/rkirtii/Pro/assets/142138548/f9ff6ebe-c7cd-46da-ab12-5f30d42b0552)

https://github-production-user-asset-6210df.s3.amazonaws.com/142138548/294856419-bb548797-bd09-4234-a49c-07542994def9.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20240108%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240108T132250Z&X-Amz-Expires=300&X-Amz-Signature=8791d8bb34dc84c24e55697270a5f3dbbd9b4f0a8fde8239fe7b41641470c426&X-Amz-SignedHeaders=host&actor_id=142138548&key_id=0&repo_id=677940319

https://github-production-user-asset-6210df.s3.amazonaws.com/142138548/294856416-f9ff6ebe-c7cd-46da-ab12-5f30d42b0552.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20240108%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240108T132323Z&X-Amz-Expires=300&X-Amz-Signature=71a85b8aec1215af6e997993de8050a542f4ea564827ee1452ff4d7c04feef29&X-Amz-SignedHeaders=host&actor_id=142138548&key_id=0&repo_id=677940319


Fetching all stores
![Screenshot from 2024-01-08 14-43-20](https://github.com/rkirtii/Pro/assets/142138548/a5f8cae9-612b-4af7-81db-7da0fa5348e7)

https://github-production-user-asset-6210df.s3.amazonaws.com/142138548/294855533-a5f8cae9-612b-4af7-81db-7da0fa5348e7.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20240108%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240108T132342Z&X-Amz-Expires=300&X-Amz-Signature=9d75a0cdb779b82e68350ce9d87c3a0668585294d9ccc75baa9e05c6cdb1e629&X-Amz-SignedHeaders=host&actor_id=142138548&key_id=0&repo_id=677940319

Deleting Mystore2
![Screenshot from 2024-01-08 14-43-38](https://github.com/rkirtii/Pro/assets/142138548/fb79aa59-e205-403a-b57f-2b94e2af73e2)

https://github-production-user-asset-6210df.s3.amazonaws.com/142138548/294855672-fb79aa59-e205-403a-b57f-2b94e2af73e2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20240108%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240108T132400Z&X-Amz-Expires=300&X-Amz-Signature=9091060ad91268bde2d3bc43b86048d85d89d62c751a9e6a2f171b56ad56603c&X-Amz-SignedHeaders=host&actor_id=142138548&key_id=0&repo_id=677940319

Fetching all items
![Screenshot from 2024-01-08 14-43-58](https://github.com/rkirtii/Pro/assets/142138548/27b4d9a6-1962-4dee-874b-1221b2d17f2b)

https://github-production-user-asset-6210df.s3.amazonaws.com/142138548/294855776-27b4d9a6-1962-4dee-874b-1221b2d17f2b.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20240108%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240108T132419Z&X-Amz-Expires=300&X-Amz-Signature=126dd1fbd9814c9249c7ae87f1f4b1ddc33921636449fbf6a23409c9e1052659&X-Amz-SignedHeaders=host&actor_id=142138548&key_id=0&repo_id=677940319
