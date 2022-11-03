<template>
  <div class="body">
    <div class="container">
      <h1>예약 페이지</h1>
      <div>
        <h3>선생님 선택</h3>
        <div>
          <div 
            class="btn-teacher"
            v-for="teacher in teachers"
            :key="teacher.name"
            :class="{'selected-teacher': teacher.isSelected}"
            @click="selectTeacher(teacher)"
          >
            {{ teacher.name }}
          </div>
        </div>
      </div>
      <hr>
      <div>
        <h3>시간 선택</h3>
        <div
          v-for="(time, idx) in times"
          :key="time" 
          class="choice-time"
          @click="choiceTime(time, idx)"
          :class="{'selected': selected[idx]}"
        >
          {{ time }}
        </div>
      </div>
    </div>
    <div class="container consult">
      <h1>상담 신청 현황</h1>
      <div>
        <h3>상담 선생님</h3>
        <p >성함 : {{ selectedTeacher }}</p>
      </div> 
      <hr>
      <div>
        <h3>예약 현황</h3>
        <p>
          시간들 : 
          <span v-if="selectedTeacher === 'Tom'" >
            <span v-for="tom in selectedTimesTom" :key="tom">{{ tom }}  |  </span>
          </span>
          <span v-else-if="selectedTeacher === 'Tony'" >
            <span v-for="tony in selectedTimesTony" :key="tony">{{ tony }}  |  </span>
          </span>
        </p>
      </div>
      <hr>
      <img src="@/assets/logo.png" alt="" width="150px">
    </div>
  </div>
</template>

<script>
export default {
  name:'ReserveConsulting',
  data () {
    return {
      times: [
        "00:00","00:30","01:00","01:30","02:00","02:30","03:00","03:30",
        "04:00","04:30","05:00","05:30","06:00","06:30","07:00","07:30",
        "08:00","08:30","09:00","09:30","10:00","10:30","11:00","11:30",
        "12:00","12:30","13:00","13:30","14:00","14:30","15:00","15:30",
        "16:00","16:30","17:00","17:30","18:00","18:30","19:00","19:30",
        "20:00","20:30","21:00","21:30","22:00","22:30","23:00","23:30",
      ],
      selected: [
        false, false, false, false, false, false, false, false,
        false, false, false, false, false, false, false, false,
        false, false, false, false, false, false, false, false,
        false, false, false, false, false, false, false, false,
        false, false, false, false, false, false, false, false,
        false, false, false, false, false, false, false, false,
      ],
      selectedTimesTom : [],
      selectedTimesTony : [],
      teachers: [
        {
          name:'Tom',
          isSelected: false,
        },        
        {
          name:'Tony',
          isSelected: false,
        },
      ],
      selectedTeacher: null
    }
  },
  methods: {
    selectTeacher (teacher) {
      this.teachers.forEach((el) => {
        if (el !== teacher) {
          el.isSelected = false
          this.selectedTeacher = null
        }
      })
      teacher.isSelected = !teacher.isSelected     
      this.teachers.forEach((el) => {
        if (el.isSelected === true) {
          this.selectedTeacher = el.name
        }
      })
    },
    choiceTime (time, idx) {
      if (this.selectedTeacher === null) {
        alert('선생님을 선택해주세요')
        return
      } else if (this.selectedTeacher === 'Tom') {
        if (this.selectedTimesTom.includes(time)) {
          this.selectedTimesTom.forEach((el, idx) => {
            if (el === time) {
              this.selectedTimesTom.splice(idx, 1)
              this.selected[idx] = false
              return
            }
          })
        } else {
          if (this.selectedTimesTom.length === 5) {
          alert('5타임까지만 신청할 수 있습니다.')
          return
        }
        this.selectedTimesTom.push(time)
        this.selected[idx] = true
        }
      } else if (this.selectedTeacher === 'Tony') {
        if (this.selectedTimesTony.includes(time)) {
          this.selectedTimesTony.forEach((el, idx) => {
            if (el === time) {
              this.selectedTimesTony.splice(idx, 1)
              this.selected[idx] = false
              return
            }
          })
        } else {
          if (this.selectedTimesTony.length === 5) {
          alert('5타임까지만 신청할 수 있습니다.')
          return
        }
        this.selectedTimesTony.push(time)
        this.selected[idx] = true
        }
      }
    },
    // isSelectedTom(time) {
    //   console.log(time)
    //   if (this.selectedTimesTom.includes(time)) {
    //     return true
    //   } else {
    //     return false
    //   }
    // },
    changeTeacher () {
      for (let i = 0; i < this.selected.length; i++) {
        this.selected[i] = false
      }
      this.selectedTimesTom = []
      this.selectedTimesTony = []
    }
    
  },
  watch: {
    selectedTeacher() {
      return this.changeTeacher()
    }
  },
}
</script>

<style>
  .body{
    display: flex;
    justify-content: center;
  }
  .container{
    width: 450px;
    height: 450px;
  }
  .consult {
    background-color: #DAE4F1;
  }
  .choice-time{
    display: inline-block;
    width: 70px;
    font-size: 20px;
    margin: 5px;
  }
  .selected{
    background-color: #DAE4F1;
  }
  .btn-teacher{
    border: 1px solid black;
    display: inline-block;
    padding: 5px 20px 5px 20px;
    margin: 10px;
  }
  .selected-teacher{
    background-color: #DAE4F1;
  }
</style>