### ERROR #1

```
vue.runtime.esm.js?2b0e:619 [Vue warn]: Avoid using non-primitive value as key, use string/number value instead.
```

### ANS #1

```
 v-for 디렉티브 사용하실 때 v-bind:key에 무언가를 연결하신 것 같은데요. 문자열이랑 숫자만 해당 값에 들어갈 수 있게 변경하시면 됩니다.
```



### ERROR #2

```
axios is not a function
```

### ANS #2

```
import axios from 'axios'
axios를 불러준다. axios 와 this.$axios 차이는???
```



### ERROR #3

```
POST http://127.0.0.1:8000/contents/workout/ 401 (Unauthorized)
```

### ANS #3

```
permission_classes([AllowAny])
누구나 접근 가능하게 해준다
```



### ERROR #4

```
TypeError: _this.saveWorkout is not a function
    at eval
```

### ANS #4

```
import { mapActions } from 'vuex'

mapActions 를 store에서 가져와야 함수가 실행되어 데이터를 저장한다.
```

