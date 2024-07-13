import streamlit as st


index = st.session_state.get("index", default=0)
st.title("Python教程")
steps = ["1.下载Python",
         "2.下载一个好用的编辑器",
         "3.创建项目",
         "4.简单认识",
         "更多:等待更新",]
page = st.selectbox(label="步骤", options=steps, index=index)
st.divider()
text = st.write
match steps.index(page):
    case 0:
        text(" ")
        text("在学习Python之前,你需要先下载一个Python.")
        text(" ")
        st.divider()
        st.header("目标:下载Python 3.11.4并安装.注意要添加到环境变量,从官网下载.")
        text("别问为什么不是最新的,因为我懒得再去重新装一遍了( •̀ ω •́ )✧")
        st.divider()
        text("出于提高自主学习能力的目的,请先尝试自行完成该目标.如遇到困难,可点击下方按钮查看详细说明.")
        if st.button("详细说明"):
            st.balloons()
            text("Python官网网址为:https://www.python.org/")
            text("下载Python")
            st.image("1.png")
            st.image("2.png")
            text("下载过慢的话,试试其他工具?(如把链接复制到迅雷中下载)")
            st.divider()
            text("安装Python")
            text("那个,Python3.11.4我已经装过了,不能重复安装,所以拿3.12演示一下,二者安装过程无区别.φ(*￣0￣)")
            for i in range(3, 7):
                st.image(f"{i}.png")
            text("第一次装的话点一下这个选项.")
            text("恭喜,安装完成!")
            text("按下windows+r,输入cmd并回车打开命令提示符,输入python")
            st.image("7.png")
            text("如图所示,你已成功安装python.🎈🎈🎈🎈")
    case 1:
        text(" ")
        text("使用优秀的编辑器是提高效率的最佳手段,可以为你提供代码补全等强大的功能.工欲善其事,必先利其器.")
        text(" ")
        st.divider()
        st.header("目标:安装一个好用的编辑器.(推荐: Pycharm)")
        st.divider()
        text("出于提高自主学习能力的目的,请先尝试自行完成该目标.如遇到困难,可点击下方按钮查看详细说明.")
        if st.button("详细说明"):
            st.balloons()
            text("此处以Pycharm为例.")
            text("Pycharm官网:https://www.jetbrains.com.cn/pycharm/download/?section=windows")
            st.image("8.png")
            text("社区版就OK,专业版要花钱,而且我想你也用不到(滑稽)")
            text("emmm...\n我不能同时装两个Pycharm,也不能卸了重装一遍,所以只能给你指一个教程了.")
            text("https://blog.csdn.net/2301_78096295/article/details/139240616")
            text("安装Chinese插件以汉化.")
            st.image("9.png")
    case 2:
        text("以Pycharm为例.请下载以下视频并观看.(当然先自己摸索一下更好)")
        st.download_button("下载视频", data=open("1.mp4", "rb"), file_name="1.mp4")
    case 3:
        text("Python中的一切都是由类构成的，不过现在你姑且可以认为分为变量(variable)、函数(function)、类(class)三大类。")
        text("Python中最基础的函数有print、input等；最基础的变量分为字符串、整数、浮点数、列表、字典、集合等。")
        text("函数调用的方法为 函数名+(参数)，注意所有标点符号均为英文字符，应仔细区分。")
        text("变量以 变量名 = 变量值 的格式赋值，注意变量名需满足如下要求：")
        text("1.字母或下划线(_)开头。")
        text("2.由字母、下划线、数字构成。")
        text("3.大小写字母不同时，变量也不相同。(如Hello和hello是两个不同的变量)")
        text()
        text("""函数：
        1.print
        打印括号中的内容。
        2.input
        先打印括号中的字符串，再获取一行输入的内容。""")

