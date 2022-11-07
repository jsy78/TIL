const locationInput = document.querySelector('#location')
const roadnameInput = document.querySelector('#roadname')
const mapContainer = document.querySelector('#map')
const mapOption = {
  center: new daum.maps.LatLng(37.537187, 127.005476), // 지도의 중심 좌표
  level: 2 // 지도의 확대 레벨
}
//지도를 미리 생성
const map = new kakao.maps.Map(mapContainer, mapOption)
// 주소-좌표 변환 객체를 생성
const geocoder = new kakao.maps.services.Geocoder()
//마커를 미리 생성
const marker = new kakao.maps.Marker({
  position: new kakao.maps.LatLng(37.537187, 127.005476),
  map: map
})
    
locationInput.addEventListener('click', function () {
  new daum.Postcode({
    oncomplete: function(data) {
      // 주소 정보를 해당 필드에 넣는다.
      locationInput.value = data.address
      roadnameInput.value = data.roadname
      // 주소로 상세 정보를 검색
      geocoder.addressSearch(data.address, function(results, status) {
        // 정상적으로 검색이 완료됐으면
        if (status === daum.maps.services.Status.OK) {
          const result = results[0] //첫번째 결과의 값을 활용
          // 해당 주소에 대한 좌표를 받아서
          const coords = new kakao.maps.LatLng(result.y, result.x)
          // 지도를 보여준다.
          mapContainer.classList.remove('d-none')
          mapContainer.classList.add('d-block')
          map.relayout()
          // 지도 중심을 변경한다.
          map.setCenter(coords)
          // 마커를 결과값으로 받은 위치로 옮긴다.
          marker.setPosition(coords)
        }
      });
    }
  }).open()
})