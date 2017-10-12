# go-coup

### Dependencies

* [Docker](https://docs.docker.com/engine/installation/)
* [Docker-Compose](https://docs.docker.com/compose/install/)
* ในกรณีที่จะรัน elasticsearch ระบบต้องมี RAM อย่างน้อย 1gb

### Build and run container(s)

* รันคำสั่งนี้บน terminal ใน project dir เพื่อทำการรัน Docker container
```shell
docker-compose up
```

* รันคำสั่งนี้บน terminal ใน project dir หลังจากทำการ git pull เพื่อทำการลง package หรือรัน migration ที่เพิ่มเข้ามาใหม่
```shell
docker-compose build
```

### Rule
* ในกรณีที่ต้องการใช้ Python package เพิ่มเติม ให้เพิ่มชื่อ package ใน requirements.txt ด้วย
* ในกรณีที่ต้องการรันคำสั่งต่างๆ บน container (เช่น pip หรือ manage.py) ให้รันคำสั่งดังกล่าวโดยพิมพ์ docker-compose exec web นำหน้าด้วย เช่น

```shell
docker-compose exec web python manage.py migrate
```

* คำสั่งที่ต้องการให้รัทุกครั้งที่ทำการรัน Docker container ให้นำไปเพิ่มในไฟล์ entrypoint.sh
* ในกรณีที่จะรันร่วมกับ nginx ให้รันโดยใช้ uwsgi หรือ gunicorn
