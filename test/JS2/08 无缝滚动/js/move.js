window.onload = function(){
    //1、不断的改变某个标签(控制所有产品，选中产品的父级ul)的left取值 -- 多次定时
    var oList = document.getElementById('list');
    var num = 0;//left取值
    var speed = -5; //默认左侧移动
    var oTimer = null;
    //复制产品的目的：保证产品移动，保证显示区域是由替补产品做填充，不镂空
    oList.innerHTML += oList.innerHTML; //oList.innerHTML = oList.innerHTML+oList.innerHTML
    oTimer = setInterval(fnMove,30);
    function fnMove(){
        // ul的left取值
        num+=speed;
        // 一直左侧移动，会后面镂空，当一份产品移动到左侧的时候（left？-1000），迅速的回到left取值为0的状态，在这个基础上再执行左侧移动
        if(num == -1000)
        {
            num=0;

        }
        //右侧按钮单击，右侧移动++的过程，左侧立刻镂空：迅速回到left取值是-1000的状态的基础之上执行右侧移动
        if(num>0)
        {
            num=-1000;
            //调试程序的代码，和本产品案例无关
            // alert(num) 调试程序的时候会打断程序的运行
            // console.log(num) 调试程序，不打断程序的运行
            // document.title = num;  选title标签设置内容
        }
        oList.style.left = num + 'px'  //'500px'
    }

    //2.1 右箭头单击，执行右侧移动
    var oBtn02 = document.getElementById('btn02');
    oBtn02.onclick = function(){
        speed = 5;
    }


    //2.2 左箭头单击，执行左侧移动
    var oBtn01 = document.getElementById('btn01');
    oBtn01.onclick = function(){
        speed = -5;
    }

    // 3.1 鼠标移入，停止定时器（停止动画）
    var oSlide = document.getElementById('slide');
    oSlide.onmouseover = function(){
        clearInterval(oTimer);
        oTimer = null;
    }

    // 3.2 鼠标离开，执行动画，再次打开定时器
    oSlide.onmouseout = function(){
        oTimer = setInterval(fnMove,30);
    }
}