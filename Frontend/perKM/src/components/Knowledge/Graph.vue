<!-- 结构,主体 -->
<template>
  <div id="main"></div>
</template>

<!-- 交互,脚本语言 -->
<script lang="ts" name="KnowledgeGraph" setup>
import { onMounted } from "vue";
import * as echarts from "echarts";
import { ref } from "vue";
import axios from "axios";

// 图数据
// const graphData = ref<any>({});

onMounted(() => {
  const chartDom = document.getElementById("main")!;
  const myChart = echarts.init(chartDom);

  // 图数据
  const graphData = ref<any>({});
  // 获取后端数据
  const get_graph_data = async () => {
    const response = await axios.get("/api/graph/data");
    console.log(response.data.data);

    const { nodes, links } = response.data.data;
    // 更新 option 数据后重新 setOption()
    option.series![0].data = nodes;
    option.series![0].edges = links;
    myChart.setOption(option);
  };

  // 力引导布局配置示例
  const option: any = {
    title: {
      text: "文档关系图",
    },
    tooltip: {},
    animationDurationUpdate: 1500, // 动画时长
    animationEasingUpdate: "quinticInOut", // 动画缓动效果

    series: [
      {
        type: "graph", // 图类型
        layout: "force", // 力引导布局
        data: [
          { name: "节点1", category: 0 }, // 节点1
          { name: "节点2", category: 0 },
          { name: "节点3", category: 1 },
          { name: "节点4", category: 1 },
        ],
        edges: [
          { source: "节点1", target: "节点2" }, // 边：节点1 → 节点2
          { source: "节点1", target: "节点3" },
          { source: "节点3", target: "节点4" },
        ],
        id: "id",
        // edgeSymbol: ['circle', 'arrow'], // 可选：显示边的方向
        roam: true, // 允许缩放和平移
        force: {
          // 力引导参数
          repulsion: 200, // 节点斥力（数值越大间距越大）
          edgeLength: 100, // 边的长度
          gravity: 0.1, // 中心引力（数值越大节点越向中心聚集）
        },
        // categories: [
        //   // 节点分类样式（可选）
        //   { name: "类别1", itemStyle: { color: "#5470c6" } },
        //   { name: "类别2", itemStyle: { color: "#91cc75" } },
        // ],
        label: {
          show: true, // 显示节点标签
        },
        lineStyle: {
          opacity: 0.9,
          width: 2,
          curveness: 0, // 边的弯曲度（0为直线）
        },
      },
    ],
  };

  myChart.setOption(option);

  get_graph_data();
});
</script>

<!-- 添加样式确保容器尺寸 -->
<style scoped>
#main {
  width: 100%;
  height: 600px;
}
</style>