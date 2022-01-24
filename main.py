import os
print('''
<!DOCTYPE html>
<html>
    <head>
        <title>Python calculator</title>
    </head>
    <style>
        *{
    margin:0px;
    padding:0px;
    box-sizing:border-box ;
    font-family:sans-serif;
}

body {
    display:flex;
    justify-content:center ;
    align-item:center;
    min-height:80;
    background:Dark Blue;
}
.calculator{
    position:relative ;
    margin-top:20px;
    border:2px solid white;
    display:grid;
}
.calculator .value{
    grid-column:span 4;
    height:120px;
    text-align:center;
    color:White;
    background:Black;
    border:3px White;
    outline:none;
    font-size:20px;
}
.calculator span{
    display:grid;
    height:60px;
    width:60px;
    color: White;
    border:1px solid white;
    background: Dark Gray;
    place-items:center;
}
.calculator span:active{
    background:Red;
    color:black;
}
.calculator span.clear{
    grid-column:span 2;
    width:120px;
    background:Black;
}
.calculator span.plus{
    grid-row:span 2;
    height:120px;
}
.calculator span.equal{
    grid-column:span 2;
    width:120px;
    background: Black;
}
.calculator span.zero{
    background: Black;
}
.calculator span.clear:active{
    background: black;
}



    </style>
    <body>
       <form class=calculator name=calc>
           <input class=value name=txt type=text readonly="">   
           <span class="num clear" onclick="document.calc.txt.value =''">C</span>
       <span class=num onclick="document.calc.txt.value +='/'">/</span>
       <span class=num onclick="document.calc.txt.value +='*'">*</span>
       <span class=num onclick="document.calc.txt.value +='7'">7</span>
       <span class=num onclick="document.calc.txt.value +='8'">8</span>
       <span class=num onclick="document.calc.txt.value +='9'">9</span>
       <span class=num onclick="document.calc.txt.value +='-'">-</span>
       <span class=num onclick="document.calc.txt.value +='4'">4</span>
       <span class=num onclick="document.calc.txt.value +='5'">5</span>
       <span class=num onclick="document.calc.txt.value +='6'">6</span>
       <span class="num plus" onclick="document.calc.txt.value +='+'">+</span>
       <span class=num onclick="document.calc.txt.value +='1'">1</span>
       <span class=num onclick="document.calc.txt.value +='2'">2</span>
       <span class=num onclick="document.calc.txt.value +='3'">3</span>
       <span class="num zero" onclick="document.calc.txt.value +='0'">0</span>
       <span class=num onclick="document.calc.txt.value +='.'">.</span>
       <span class="num equal" onclick="document.calc.txt.value =eval(calc.txt.value)">=</span>
      
       </form>
    </body>
</html>''')

os.system("touch file.png")

print("<style>img{display:none;}</style>")
