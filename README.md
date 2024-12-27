# README

## 生成基于圆形的相机标定图案

### 简介

该项目旨在生成基于圆形的相机标定图案，允许用户通过调整图像的分辨率和圆之间的间隔来调节排列结构。使用tkinter库中的滑块来动态调整生成图像的参数，并通过PyInstaller进行打包，便于分发和使用。

### 使用方法

1. **生成图案**：
   - 该项目首先生成一个白底黑色实心圆的图案。
   - 图案的分辨率和圆之间的间隔可以通过程序中的参数进行调整。

2. **调节参数**：
   - 使用tkinter库中的滑块来动态调节图像生成中的参数，包括图像的分辨率和圆之间的间隔。

3. **打包程序**：
   - 使用PyInstaller将Python脚本打包成独立的可执行文件。
   - 打包命令：`pyinstaller -F -w circle.py`
   - 注意：在打包过程中可能会遇到运行时错误。如果出现这种情况，请在生成的.spec文件中修改`hiddenimports=[]`为`hiddenimports=['tkinter','PIL','PIL._tkinter_finder']`，然后对.spec文件重新编译：`pyinstaller circle.spec`。

4. **运行程序**：
   - 打包成功后，可以通过以下命令运行程序：`./dist/circle --s 1728 1080 --n data`
   - 其中，`--s 1728 1080`指定了图像的分辨率为1728x1080，`--n data`指定了其他可能的参数（具体含义根据程序实现而定）。

### 参考资料

- [CSDN博客1](https://blog.csdn.net/weixin_40755306/article/details/88880234)：提供了关于使用tkinter和PyInstaller的详细指导。
- [CSDN博客2](https://blog.csdn.net/dcjklkmm/article/details/135940123?spm=1001.2014.3001.5502)：可能包含关于图像处理或相机标定图案生成的额外信息。

### 注意事项

- 在运行程序之前，请确保已经安装了Python和PyInstaller，以及tkinter和PIL（Pillow）库。
- 如果在运行过程中遇到任何问题，请检查.spec文件的配置是否正确，并尝试重新编译。
- 该项目仅供参考和学习之用，具体使用时可能需要根据实际需求进行修改和扩展。
