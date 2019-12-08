export default {
  title: {
    text: '',
    x: 'center'
  },
  toolbox: {
    show: true,
    orient: "vertical",
    left: "right",
    top: "center",
    feature: {
      mark: { show: true },
      dataView: { show: true, readOnly: false },
      magicType: { show: true, type: ["line", "bar", "stack", "tiled"] },
      restore: { show: true },
      saveAsImage: { show: true }
    }
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
