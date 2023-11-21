# ClientEvents.paintScreen

## Basic info

- Valid script types: [CLIENT]

- Has result? ✘

- Event class: [PaintScreenEventJS](https://github.com/KubeJS-Mods/KubeJS/tree/1902/common/src/main/java/dev/latvian/mods/kubejs/client/painter/screen/PaintScreenEventJS.java)

### Available fields:

| Name | Type | Static? |
| ---- | ---- | ------- |
| mouseX | int | ✘ |
| mouseY | int | ✘ |
| width | int | ✘ |
| height | int | ✘ |
| inventory | boolean | ✘ |
| mc | Minecraft | ✘ |
| font | Font | ✘ |
| matrices | PoseStack | ✘ |
| tesselator | Tesselator | ✘ |
| buffer | BufferBuilder | ✘ |
| delta | float | ✘ |
| screen | Screen | ✘ |

Note: Even if no fields are listed above, some methods are still available as fields through *beans*.

### Available methods:

| Name | Parameters | Return type | Static? |
| ---- | ---------- | ----------- | ------- |
| scale | float, float |  | void | ✘ |
| scale | float |  | void | ✘ |
| text | Component, float, float, int, boolean |  | void | ✘ |
| rectangle | float, float, float, float, float, int |  | void | ✘ |
| rectangle | float, float, float, float, float, int, float, float, float, float |  | void | ✘ |
| rawText | FormattedCharSequence, float, float, int, boolean |  | void | ✘ |
| alignY | float, float, int |  | float | ✘ |
| getVariables |  |  | VariableSet | ✘ |
| rotateRad | float |  | void | ✘ |
| alignX | float, float, int |  | float | ✘ |
| rotateDeg | float |  | void | ✘ |
| translate | double, double |  | void | ✘ |
| scale | float, float, float |  | void | ✘ |
| multiply | Quaternion |  | void | ✘ |
| push |  |  | void | ✘ |
| pop |  |  | void | ✘ |
| begin | VertexFormat$Mode, VertexFormat |  | void | ✘ |
| end |  |  | void | ✘ |
| resetShaderColor |  |  | void | ✘ |
| multiplyWithMatrix | Matrix4f |  | void | ✘ |
| beginQuads | VertexFormat |  | void | ✘ |
| beginQuads | boolean |  | void | ✘ |
| setShaderInstance | Supplier<ShaderInstance> |  | void | ✘ |
| translate | double, double, double |  | void | ✘ |
| getMatrix |  |  | Matrix4f | ✘ |
| setShaderColor | float, float, float, float |  | void | ✘ |
| setShaderTexture | ResourceLocation |  | void | ✘ |
| vertex | Matrix4f, float, float, float, int, float, float |  | void | ✘ |
| vertex | Matrix4f, float, float, float, int |  | void | ✘ |
| setPositionColorTextureShader |  |  | void | ✘ |
| setPositionColorShader |  |  | void | ✘ |
| bindTextureForSetup | ResourceLocation |  | void | ✘ |
| getEntity |  |  | Entity | ✘ |
| getPlayer |  |  | LocalPlayer | ✘ |
| hasGameStage | String |  | boolean | ✘ |
| addGameStage | String |  | void | ✘ |
| removeGameStage | String |  | void | ✘ |
| getLevel |  |  | Level | ✘ |
| getServer |  |  | MinecraftServer | ✘ |
| exit | Object |  | Object | ✘ |
| exit |  |  | Object | ✘ |
| cancel | Object |  | Object | ✘ |
| cancel |  |  | Object | ✘ |
| success | Object |  | Object | ✘ |
| success |  |  | Object | ✘ |


### Documented members:

- `boolean hasGameStage(String var0)`

  Parameters:
  - var0: String

```
Checks if the player has the specified game stage
```

- `void addGameStage(String var0)`

  Parameters:
  - var0: String

```
Adds the specified game stage to the player
```

- `void removeGameStage(String var0)`

  Parameters:
  - var0: String

```
Removes the specified game stage from the player
```

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
ClientEvents.paintScreen((event) => {
	// This space (un)intentionally left blank
});
```

