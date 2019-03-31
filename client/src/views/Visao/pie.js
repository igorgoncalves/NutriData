export default {
  title: {
    text: '',
    x: 'center'
  },
  tooltip: {
    trigger: 'item',
    formatter: '{a} <br/>{b} : {c} ({d}%)'
  },
  legend: {
    type: 'scroll',
    orient: 'vertical',
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
      center: ['35%', '60%'],
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
