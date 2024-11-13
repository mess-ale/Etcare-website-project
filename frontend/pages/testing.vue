<template>
    <div>
      <h1>GraphQL Data</h1>
      <p>{{ data }}</p>
    </div>
  </template>
  
  <script>
  import { useQuery } from '@vue/apollo-composable';
  import gql from 'graphql-tag';
  
  export default {
    setup() {
      const { result } = useQuery(gql`
        query {
          hello {
            message
          }
        }
      `);
  
      return { data: result.value };
    },
  };
  </script>
  