<template>
  <div id="reserve-div">
    <div>
      <h2>예약 페이지</h2>
      <h3>시간 선택</h3>
      <div 
        v-for="time in times" 
        :key="time" 
        class="time"
        @click="reserve"  
      >
        {{ time }}
      </div>
      <hr>
      <h4>
        선택 시간 : <span v-for="reserve in reserved" :key="reserve">{{ reserve }}</span>
      </h4>
    </div>
  </div>
</template>

<script>
export default {
  name:'ReserveTime',
  data: function() {
    return{
      times: [
        "09:00","09:30","10:00","10:30","11:00","11:30","12:00","12:30","13:00","13:30",
        "14:00","14:30","15:00","15:30","16:00","16:30","17:00","17:30","18:00","18:30",
        "19:00","19:30","20:00","20:30","21:00","21:30","22:00","22:30","23:00","23:30",
      ],
      reserved: []
    }
  },
  methods: {
    reserve: function (e) {
      if (this.reserved.length > 4) {
        alert('5타임까지만 신청할 수 있습니다.')
      } else if (this.reserved.includes(e.target.innerHTML)) {
        this.reserved.forEach((el, idx) => {
          if (el === e.target.innerHTML) {
            this.reserved.splice(idx, 1)
          }
        })
        e.target.classList.remove('selected')
      } else {
        this.reserved.push(e.target.innerHTML)
        e.target.classList.add('selected')
      }
    }
  }
}
</script>

<style>
  #reserve-div{
    width: 500px;
    border: 1px solid gainsboro;
    box-shadow: 1px 1px grey;
  }
  .time{
    display: inline-block;
    margin: 5px;
    width: 50px;
    border: 1px solid black;
  }
  .selected{
    background-color: aqua;
  }
</style>