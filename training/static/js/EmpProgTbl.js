export default {
    props: {
      availableProgramList: []
    },
    template: `
  <div v-if="availableProgramList.length ==0">
    <p>None</p>
  </div>
  <div v-else>
  <table v-bind:availableProgramList="availableProgramList">
    <tr>
      <th>Code</th>
      <th>Description</th>
      <th>Minimum Eligibility</th>
      <th>Maximum Eligibility</th>
      <th>Type</th>
    </tr>

    <tr v-for="prog in availableProgramList" :key="prog.code">
      <td>{{prog.code}}</td>
      <td>{{prog.description}}</td>
      <td>{{prog.minimumeligibility.description}}</td>
      <td>{{prog.maximumeligibility.description}}</td>
      <td>{{prog.type.description}}</td>
    </tr>
   </table>
  </div>  
    `
  }
