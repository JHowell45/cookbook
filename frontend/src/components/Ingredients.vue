<template>
    <div class="ingredients_container">
        <div class="ingredients_content">
            <h1>Ingredients</h1>
            <ul class="ingredients_list">
                <li v-for="ingredient in ingredients" :key="ingredient.id">
                    <h2>{{ ingredient.name }}</h2>
                    <p>{{ ingredient.description }}</p>
                    <!-- <button @click="toggleIngredient(ingredient)">
                        {{ ingredient.completed ? 'Undo' : 'Complete' }}
                    </button> -->
                    <!-- <button @click="deleteIngredient(ingredient)">Delete</button> -->
                </li>
            </ul>
        </div>
    </div>
</template>

<script>
    import axios from 'axios';

    export default {
        data() {
            return {
                // ingredients
                ingredients: ['']
            }
        },
        methods: {
            async getData() {
                try {
                    // fetch ingredients
                    const response = await axios.get('http://backend:9000/api/ingredients/');
                    // set the data returned as ingredients
                    this.ingredients = response.data; 
                } catch (error) {
                    // log the error
                    console.log(error);
                }
            },
        },
        created() {
            // Fetch tasks on page load
            this.getData();
        }
    }
</script>