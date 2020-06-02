# Discord TRPG Bot

Discord上でTRPG(CoC)をプレイする際の補助Bot

# Requirements
- discord 1.0.1
- discord.py 1.3.3 (voice)
- ffmpeg
- opus

# Installation
```requirements.txt
discord==1.0.1
discord.py[voice]==1.3.3
```

```bash
pip install -r requirements.txt
```

# Commands

## セッションを立てる
`!create`

ゲームマスターがセッションを立てるときに使用するコマンドです。
セッションを立てた人がゲームマスターとして登録されます。

## セッションに参加する
`!join`

ゲームマスター以外の参加者はこのコマンドを用いてセッションに参加する

## セッションを開始する
`!start`

参加者が揃いセッションの準備が完了するとこのコマンドを用いてセッションを開始する

## セッションを終了する
`!close`

セッションが全て終了した際に使用し、ゲームのログをファイルに書き出す

## セッション(全体)のログを書き出す
`!sessionlog`

セッションの現在時点でのログファイルを書き出す

## セッション(個人)のログを書き出す
`!mylog`

コマンド使用者の現在時点でのログファイルを書き出す

## サイコロを振る

### カスタムダイスを振る
`!dice` `!d`

3D6(6面ダイスを3つ振る)

`!dice dice_count dice_max`

任意の面のダイス(dice_max)を任意の個数(dice_count)振る

使用例
```
!dice     --> 3D6
!dice 2 6 --> 2D6
!dice 3 4 --> 3D4
```

### 100面ダイスを振る
`!d100` or `!dd`

100面ダイスを1つ振る

`!d100 limit`

100面ダイスを1つ振り成功するか判定(limit %の成功率)する

使用例
```
!d100     --> 1D100を振る
!d100 60  --> 1D100を振った結果60%の成功率で成功するかを判定する
!d100 80  --> 1D100を振った結果80%の成功率で成功するかを判定する
```
### シークレットダイスを振る
`!seacret` or `!sd`

1d100の結果をコマンド使用者のDMに送信する

# Author
- いなたつ
- [Twitter](https://twitter.com/_inatatsu_csg_)
- [Qiita](https://qiita.com/inatatsu_csg)