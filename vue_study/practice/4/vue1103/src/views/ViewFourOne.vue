<template>
  <div>
    <div id="reserve">
      <ReserveTime/>
    </div>
  </div>
</template>

<script>
import ReserveTime from '@/components/ReserveTime';

export default {
  name: 'AboutView',
  components: {
    ReserveTime
  }
}
</script>

<style>
  #reserve{
    display: flex;
    justify-content: center;
  }
</style>