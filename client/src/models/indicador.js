import Amostra from "./amostra";

export default class Indicador {
  constructor({ nome, amostras }) {
    amostras = amostras || [];
    
    this.nome = nome;    
    this.amostras = amostras.map((amostra) => new Amostra({ ...amostra }));
  }
}
