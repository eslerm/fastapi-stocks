import { useD3 } from './hooks/useD3';
import React from 'react';
import * as d3 from 'd3';


function Graph({ data }) {

  const ref = useD3(
    (svg) => {

      data.forEach(function(d) {
        d.date = d3.timeParse("%Y-%m-%d")(d.date);
        d.price = +d.price;
        return d;
      });

      // useLayoutEffect
      const margin = {top: 0, right: 30, bottom: 30, left: 0};
      const width = 700 - margin.left - margin.right;
      const height = 400 - margin.top - margin.bottom;


      const wrapper = (g) =>
        g.attr("transform", `translate(${margin.left},${margin.top})`);


      const x = d3.scaleTime()
        .domain(d3.extent(data, function(d) { return d.date; }))
        .range([ 0, width ]);
      const xAxis = (g) =>
        g.attr("transform", `translate(0, ${height})`).call(
          d3
            .axisBottom(x)
	);
      svg.select(".x-axis").call(xAxis);


      const y = d3.scaleLinear()
        .domain([0, d3.max(data, function(d) { return +d.price; })])
        .range([ height, 0 ]);
      const yAxis = (g) =>
        g.attr("transform", `translate(${width}, 0)`).call(
          d3
            .axisRight(y)
	);
      svg.select(".y-axis").call(yAxis);


      const linePath = (path) =>
	path
        .datum(data)
        .attr("fill", "none")
        .attr("stroke", "#3b88c3")
        .attr("stroke-width", 1.5)
        .attr("d", d3.line()
          .x(function(d) { return x(d.date) })
          .y(function(d) { return y(d.price) }));

      svg.select(".path").call(linePath);

    },
    [data.length]
  );

  return (
    <svg
      ref={ref}
      style={{
        height: 430,
        width: 730,
        marginRight: "0px",
        marginLeft: "0px",
      }}
    >
      <g transform="translate(0,0)">
        <g className="x-axis" />
        <g className="y-axis" />
        <path className="path" />
      </g>
    </svg>
  );
}


export default Graph;
