import React from 'react';
import './Footer.css';

function Footer() {
  return (
    <footer>
      <p>
        Powered by <a href="https://fastapi.tiangolo.com/" target="_blank" rel="noreferrer">FastAPI</a>, <a href="https://reactjs.org/" target="_blank" rel="noreferrer">React.js</a>, <a href="https://d3js.org/" target="_blank" rel="noreferrer">D3.js</a> and <a href="https://aws.amazon.com/" target="_blank" rel="noreferrer">AWS</a><br />
        Built, operated, and designed by <a href="https://markesler.com" title="Mark Esler">Mark Esler</a>
      </p>
    <script>
const margin = {top: 0, right: 30, bottom: 30, left: 0},
    width = 700 - margin.left - margin.right,
    height = 400 - margin.top - margin.bottom;

const svg = d3.select("#graph")
  .append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
  .append("g")
    .attr("transform", `translate(${margin.left},${margin.top})`);

d3.json("/history/CL=F").then(function(data) {
  data.forEach(function(d) {
    //d.date = d3.timeParse("%Y-%m-%dT:00:00")(d.date);
    d.date = d3.timeParse("%Y-%m-%dT00:00:00")(d.date);
    d.price = +d.price;
    return d;
  });

  const x = d3.scaleTime()
    .domain(d3.extent(data, function(d) { return d.date; }))
    .range([ 0, width ]);
  svg.append("g")
    .attr("transform", `translate(0, ${height})`)
    .call(d3.axisBottom(x));

  const y = d3.scaleLinear()
    .domain([0, d3.max(data, function(d) { return +d.price; })])
    .range([ height, 0 ]);
  svg.append("g")
    .attr("transform", `translate(${width}, 0)`)
    .call(d3.axisRight(y));

  svg.append("path")
    .datum(data)
    .attr("fill", "none")
    .attr("stroke", "#3b88c3")
    .attr("stroke-width", 1.5)
    .attr("d", d3.line()
      .x(function(d) { return x(d.date) })
      .y(function(d) { return y(d.price) })
      )

})
</script>
    </footer>
  );
}

export default Footer;
