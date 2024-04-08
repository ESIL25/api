import streamlit as st
import streamlit.components.v1 as components

# 앱 제목 설정
st.title('지도 API 실습')

# HTML 및 자바스크립트를 포함한 지도를 표시
components.html(
    """
    <!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>브이월드 오픈API</title>
    <script src="https://map.vworld.kr/js/map/OpenLayers-2.13/OpenLayers-2.13.js"></script>
    <script src="https://map.vworld.kr/js/apis.do?type=Base&apiKey=02FEC135-0495-3479-A9D3-1398A00EDBA0"></script>
    <script>
        var map;
        function init() {
            var options = {
                projection: new OpenLayers.Projection("EPSG:900913"),
                displayProjection: new OpenLayers.Projection("EPSG:4326"),
                units: "m",
                numZoomLevels: 21,
                maxResolution: 156543.0339,
                maxExtent: new OpenLayers.Bounds(-20037508.34, -20037508.34, 20037508.34, 20037508.34)
            };
            map = new OpenLayers.Map('map', options);

            // 지도 레이어 추가
            var vBase = new vworld.Layers.Base('VBASE');
            var vSAT = new vworld.Layers.Satellite('VSAT');
            var vHybrid = new vworld.Layers.Hybrid('VHYBRID');
            var vWhite = new vworld.Layers.White('VWHITE');
            var vMidnight = new vworld.Layers.Midnight('VMIDNIGHT');

            map.addLayers([vBase, vSAT, vHybrid, vWhite, vMidnight]);

            map.addControl(new OpenLayers.Control.LayerSwitcher());
            map.zoomToExtent(map.getMaxExtent());

            map.addControl(new OpenLayers.Control.PanZoomBar());
            map.addControl(new OpenLayers.Control.Navigation());
            map.addControl(new OpenLayers.Control.Attribution({separator: " "}));
        }

        function deleteLayerByName(name) {
            var layer = map.getLayerByName(name);
            if (layer) {
                map.removeLayer(layer);
            }
        }
    </script>
    <style>
        .olControlAttribution { right: 20px; }
        .olControlLayerSwitcher { right: 20px; top: 20px; }
    </style>
</head>
<body onload="init()">
    <div id="map" style="height: 600px;"></div>
    <div>
        <button type="button" onclick="deleteLayerByName('VHYBRID');">레이어 삭제하기</button>
    </div>
</body>
</html>

    """,
    height=800
)
