# enviro_indoors_sensor_custom
https://github.com/pimoroni/enviroplus-python のスクリプトを改良したやつ

- weather_custom.py
  - 温度、気圧、湿度を取得するシンプルなプログラム
  - 計測のばらつきを低減するために、複数回取得して平均値を計算している
  - 実行時に取得回数と取得間隔を変更できる
- weather_viewer.py
  - 基本的な構造はweather_custom.pyと同じ
  - モニターにも表示できるようになっている
