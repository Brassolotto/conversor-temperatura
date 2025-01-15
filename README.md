# Conversor de Temperatura em Python

## 📝 Descrição
Um programa que converte temperaturas entre as escalas Celsius, Fahrenheit e Kelvin. Desenvolvido em Python puro, oferece uma interface via linha de comando simples e intuitiva.

## 🌡️ Funcionalidades
- Conversão entre todas as principais escalas de temperatura:
  - Celsius para Fahrenheit
  - Celsius para Kelvin
  - Fahrenheit para Celsius
  - Fahrenheit para Kelvin
  - Kelvin para Celsius
  - Kelvin para Fahrenheit
- Resultados com precisão de duas casas decimais
- Interface via linha de comando
- Validação de entradas

## 📋 Pré-requisitos
- Python 3.6 ou superior instalado
- Não requer bibliotecas externas

## 🔧 Como executar
1. Clone este repositório:
```bash
git clone https://github.com/Brassolotto/conversor-temperatura.git
```

2. Navegue até o diretório do projeto:
```bash
cd conversor-temperatura
```

3. Execute o programa:
```bash
python conversor_temperatura.py
```

## 📖 Como usar
1. Escolha uma opção de conversão (1-6)
2. Digite a temperatura que deseja converter
3. O resultado será exibido formatado
4. Para sair, escolha a opção 0

## 🎯 Exemplo de uso
```
Conversor de Temperatura
1. Celsius para Fahrenheit
2. Celsius para Kelvin
3. Fahrenheit para Celsius
4. Fahrenheit para Kelvin
5. Kelvin para Celsius
6. Kelvin para Fahrenheit
0. Sair

Escolha uma opção (0-6): 1
Digite a temperatura: 25
25°C = 77.00°F
```

## ⚠️ Tratamento de Erros
- Validação de entrada numérica
- Proteção contra entradas inválidas
- Mensagens de erro claras e informativas

## 🔍 Estrutura do Código
```
conversor_temperatura.py
├── Funções de conversão
│   ├── celsius_para_fahrenheit()
│   ├── celsius_para_kelvin()
│   ├── fahrenheit_para_celsius()
│   ├── fahrenheit_para_kelvin()
│   ├── kelvin_para_celsius()
│   └── kelvin_para_fahrenheit()
└── Função main()
```

## 🤝 Contribuindo
Contribuições são bem-vindas! Para contribuir:
1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/NovaFeature`)
3. Commit suas mudanças (`git commit -m 'Adicionando nova feature'`)
4. Push para a branch (`git push origin feature/NovaFeature`)
5. Abra um Pull Request

## ✨ Melhorias Futuras
- [ ] Interface gráfica
- [ ] Validação de temperaturas impossíveis
- [ ] Histórico de conversões
- [ ] Suporte a mais unidades de temperatura
- [ ] Conversão em lote
- [ ] Exportação de resultados

## 📝 Licença
Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 👤 Autor
Seu Nome
- GitHub: [@seu-usuario](https://github.com/Brassolotto)
- LinkedIn: [@seu-linkedin](https://linkedin.com/in/ricardo-brassolotto)

---
⌨️ com ❤️ por [Rick Brassolotto] 😊