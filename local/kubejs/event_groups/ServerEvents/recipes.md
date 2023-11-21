# ServerEvents.recipes

## Basic info

- Valid script types: [SERVER]

- Has result? ✘

- Event class: [RecipesEventJS](https://github.com/KubeJS-Mods/KubeJS/tree/1902/common/src/main/java/dev/latvian/mods/kubejs/recipe/RecipesEventJS.java)

### Available fields:

| Name | Type | Static? |
| ---- | ---- | ------- |
| SKIP_ERROR | Pattern | ✔ |
| originalRecipes | Map<ResourceLocation, RecipeJS> | ✘ |
| addedRecipes | Collection<RecipeJS> | ✘ |
| failedCount | AtomicInteger | ✘ |
| takenIds | Map<ResourceLocation, RecipeJS> | ✘ |
| shaped | RecipeTypeFunction | ✘ |
| shapeless | RecipeTypeFunction | ✘ |
| smelting | RecipeTypeFunction | ✘ |
| blasting | RecipeTypeFunction | ✘ |
| smoking | RecipeTypeFunction | ✘ |
| campfireCooking | RecipeTypeFunction | ✘ |
| stonecutting | RecipeTypeFunction | ✘ |
| smithing | RecipeTypeFunction | ✘ |

Note: Even if no fields are listed above, some methods are still available as fields through *beans*.

### Available methods:

| Name | Parameters | Return type | Static? |
| ---- | ---------- | ----------- | ------- |
| remove | RecipeFilter |  | void | ✘ |
| custom | JsonObject |  | RecipeJS | ✘ |
| stage | RecipeFilter, String |  | void | ✘ |
| getRecipes |  |  | Map<String, Object> | ✘ |
| replaceInput | RecipeFilter, ReplacementMatch, InputReplacement |  | void | ✘ |
| replaceOutput | RecipeFilter, ReplacementMatch, OutputReplacement |  | void | ✘ |
| customFilter | Predicate<RecipeKJS> |  | RecipeFilter | ✘ |
| addRecipe | RecipeJS, boolean |  | RecipeJS | ✘ |
| setItemErrors | boolean |  | void | ✘ |
| printExamples | String |  | void | ✘ |
| printAllTypes |  |  | void | ✘ |
| printTypes |  |  | void | ✘ |
| getRecipeFunction | String |  | RecipeTypeFunction | ✘ |
| runInParallel | Runnable |  | void | ✔ |
| runInParallel | Callable<T> |  | T | ✔ |
| containsRecipe | RecipeFilter |  | boolean | ✘ |
| recipeStream | RecipeFilter |  | Stream<RecipeJS> | ✘ |
| forEachRecipe | RecipeFilter, Consumer<RecipeJS> |  | void | ✘ |
| countRecipes | RecipeFilter |  | int | ✘ |
| findRecipes | RecipeFilter |  | Collection<RecipeJS> | ✘ |
| findRecipeIds | RecipeFilter |  | Collection<ResourceLocation> | ✘ |
| exit | Object |  | Object | ✘ |
| exit |  |  | Object | ✘ |
| cancel | Object |  | Object | ✘ |
| cancel |  |  | Object | ✘ |
| success | Object |  | Object | ✘ |
| success |  |  | Object | ✘ |


### Documented members:

- `Object exit(Object var0)`

  Parameters:
  - var0: Object

```
Stops the event with the given exit value. Execution will be stopped **immediately**.

`exit` denotes a `default` outcome.
```

- `Object exit()`
```
Stops the event with default exit value. Execution will be stopped **immediately**.

`exit` denotes a `default` outcome.
```

- `Object cancel(Object var0)`

  Parameters:
  - var0: Object

```
Cancels the event with the given exit value. Execution will be stopped **immediately**.

`cancel` denotes a `false` outcome.
```

- `Object cancel()`
```
Cancels the event with default exit value. Execution will be stopped **immediately**.

`cancel` denotes a `false` outcome.
```

- `Object success(Object var0)`

  Parameters:
  - var0: Object

```
Stops the event with the given exit value. Execution will be stopped **immediately**.

`success` denotes a `true` outcome.
```

- `Object success()`
```
Stops the event with default exit value. Execution will be stopped **immediately**.

`success` denotes a `true` outcome.
```



### Example script:

```js
ServerEvents.recipes((event) => {
	// This space (un)intentionally left blank
});
```

