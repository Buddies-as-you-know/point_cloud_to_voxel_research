


# やること
- [x] ハードコーディング解消
- [x] 点群をボクセル化してボクセル一つを大きくする。
- [ ] voxelのmesh化を行う
- [ ] Fbxへの変換を行う
- [ ] unreal engineへの追加

# メモ書き
- 点群をボクセル化したあとはObjectにしたい
  - 理由:
- [FBXをインポートするときにエラーが出る。](https://forums.unrealengine.com/t/topic/452182)
  - DCCツールからFBXを出力する際に、SmoothingGroupを出力するように設定してください
  - https://imoue.hatenablog.com/entry/2016/07/16/232417
- [fbx変換可能](https://docs.aspose.com/3d/net/supported-file-formats/#:~:text=%E3%80%9032%E2%80%A0FBX%E2%80%A0docs.fileformat.com%E3%80%91%20Autodesk%20FBX%20format.%20,5%2C%20both%20ASCII%2FBinary)
- mesh化にかなりの時間がかかりそう
  - https://tecsingularity.com/open3d/bpa/
  - https://tecsingularity.com/open3d/normalestimation/
  - [meshlabでのマーチングキューブアルゴリズム](https://www.rccm.co.jp/icem/pukiwiki/index.php?%E7%82%B9%E7%BE%A4%E3%81%8B%E3%82%89%E3%83%9E%E3%83%BC%E3%83%81%E3%83%B3%E3%82%B0%E3%82%AD%E3%83%A5%E3%83%BC%E3%83%96%E3%82%B9%28APSS%29%E3%81%A7%E9%9D%A2%E3%82%92%E4%BD%9C%E6%88%90%28MeshLab%29)
# 参考文献
