import { createApp, h } from 'vue'
import App from './App.vue'
import router from './router'
import { ApolloClient, InMemoryCache } from '@apollo/client/core'
import { createApolloProvider } from '@vue/apollo-option'

const cache = new InMemoryCache()

const apolloClient = new ApolloClient({
    cache,
    uri: 'http://localhost:8000/graphql',
})

const apolloProvider = createApolloProvider({
    defaultClient: apolloClient,
    wsEndpoint: null,
})

const app = createApp(
    {
        render: () => h(App),
    }
)

app.use(router)
app.use(apolloProvider)
app.mount('#app')
