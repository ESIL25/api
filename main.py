import streamlit as st
import streamlit.components.v1 as components

# 앱 제목 설정
st.title('지도 API 실습')

# HTML 및 자바스크립트를 포함한 지도를 표시
components.html(
    """
    <html>
    <head>
    <title>vworld 지도 예제</title>
    <script type="text/javascript" src="https://map.vworld.kr/js/vworldMapInit.js.do?version=2.0&apiKey=02FEC135-0495-3479-A9D3-1398A00EDBA0"></script>
    </head>
    <body>
    <div id="vworldMap" style="width:100%;height:80vh;"></div>
    <script type="text/javascript">
    var map;
    function init() {
        var vw = new VWorldMap('vworldMap');
        vw.setMapMode('2d');
        map = vw.getMap();
    }
    window.onload = init;
    </script>
    </body>
    </html>
    """,
    height=800
)
