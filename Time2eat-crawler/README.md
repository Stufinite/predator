# Time-To-Eat (吃飯爬蟲)[![Build Status](https://travis-ci.org/Stufinite/Time2eat-crawler.svg?branch=master)](https://travis-ci.org/Stufinite/Time2eat-crawler )

此爬蟲會將Gomaji網頁上面的所有餐廳資訊轉成json檔


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisities

```
sudo apt-get update
sudo apt-get install python3 python3-dev
```

### Installing

```
git clone https://github.com/Stufinite/Time-To-Dinner.git
make install
```

## Run

* `python3 Crawler_of_restaurant.py <fileName.json>`
* Or `make test` (This command must be executed in root directory of this project)

### Result

* json結果
  *
  ```
  {
    "台中": {
      "下午茶": [
        {
          "restaurant": "哈根達斯 Häagen-Dazs(敦南旗鑑店)",
          "url": "http://www.gomaji.com/Taipei_p127829.html",
          "地址": "台北市大安區敦化南路一段173號(近忠孝敦化捷運)\r\t\t\t\t\t\t\t\t\t\t\t",
          "營業時間": "週一至週四、週日  11:00~23:00 週五至週六 11:00~23:30",
          "電話": "(02)2776-9553"
        },
        {
          "restaurant": "J coffee",
          "url": "http://www.gomaji.com/Taichung_p126863.html",
          "地址": "台中市中區雙十路一段35-14號(近台中火車站)\r\t\t\t\t\t\t\t\t\t\t\t",
          "營業時間": "週一至週日 06:00~21:00 每週四公休",
          "電話": "(04)2220-0072"
        }
        ...
      ]
    }
  }
  ```


* 餐廳圖片
  * ![restaurant](demoJpg/隱藏丼飯達人(崇德店).jpg)


## Built With

* python3.4

## Versioning

For the versions available, see the [tags on this repository](https://github.com/Stufinite/Time-To-Dinner/releases).

## Contributors
* **張泰瑋** [david](https://github.com/david30907d)
* **柯秉廷**

## License

## Acknowledgments

* 感謝gomaji的資料
