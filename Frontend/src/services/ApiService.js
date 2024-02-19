import axios from "axios";

export default function getproperty(){
    return axios.get('http://127.0.0.1:8000/api')
    .then(res => {
        return res.data
    })   
}