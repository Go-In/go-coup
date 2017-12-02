# go-coup

### Dependencies

* [Docker](https://docs.docker.com/engine/installation/)
* [Docker-Compose](https://docs.docker.com/compose/install/)
* ในกรณีที่จะรัน elasticsearch ระบบต้องมี RAM อย่างน้อย 1gb

### Usage Tools
* Django 1.11
* Go Programming Language
* NodeJS
* PostgreSQL
* MongoDB
* Redis
* Memcached

### Build and run container(s)

* รันคำสั่งนี้บน terminal ใน project dir เพื่อทำการรัน Docker container
```shell
docker-compose up
```
* ในกรณีที่อยู่ในระหว่างการ development ให้ใช้ django built-in server เป็นหลัก และใช้ uwsgi ร่วมกับ nginx ในระหว่างช่วง deployment
* uwsgi ถูก config ไว้ให้สื่อสารกับ nginx ผ่านทาง socket ถ้าต้องการจะทดสอบการเข้าเว็บผ่าน uwsgi โดยตรง จะต้องเข้าไปแก้ไฟล์ config ก่อน

### Rule
* ในกรณีที่ต้องการใช้ Python package เพิ่มเติม ให้เพิ่มชื่อ package ใน requirements.txt ด้วย
* ในกรณีที่ต้องการรันคำสั่งต่างๆ บน container (เช่น pip หรือ manage.py) ให้รันคำสั่งดังกล่าวโดยพิมพ์ docker-compose exec web นำหน้าด้วย เช่น

```shell
docker-compose exec web python manage.py migrate
```

* คำสั่งที่ต้องการให้รัทุกครั้งที่ทำการรัน Docker container ให้นำไปเพิ่มในไฟล์ entrypoint.sh
* ในกรณีที่จะรันร่วมกับ nginx ให้รันโดยใช้ uwsgi
