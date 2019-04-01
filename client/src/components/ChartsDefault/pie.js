export default {
  title: {
    text: '',
    x: 'center'
  },
  tooltip: {
    trigger: 'item',
    formatter: '{b} : {c} ({d}%)'
  },
  legend: {
    type: 'scroll',
    orient: 'horizontal',
    right: 20,
    top: 20,
    bottom: 20,
    data: []
  },
  series: [
    {
      name: '',
      type: 'pie',
      radius: '55%',
      center: ['50%', '60%'],
      data: [
      ],
      itemStyle: {
        emphasis: {
          shadowBlur: 10,
          shadowOffsetX: 0,
          shadowColor: 'rgba(0, 0, 0, 0.5)'
        }
      }
    }
  ]
}
