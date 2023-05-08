# ECA2022_2

Códigos da disciplina de Técnicas de Programação II do curso de Eng. de Cart e de Agrimensura

Ano 2023 


# Conecta Canaã

O aplicativo Conecta Canaã tem o seu público alvo os moradores da cidade Canaã dos Carajás. Estes podem se cadastrar no app e utilizá-lo para abrir ocorrências que serão reportadas no sistema web da prefeitura. O software está disponível para download na AppStore ou PlayStore.

*******
## Tabela de conteúdo

   1. [Instalação em ambiente arm](#arm)
   2. [Instalação em ambiente intel](#intel)

*******

<div id='arm'/>  

## Instalação em ambiente arm

### Instalar dependências
`npm install`

### Configure watchamn
`echo 999999 | sudo tee -a /proc/sys/fs/inotify/max_user_watches`

### Iniciar react
`npx react-native start`

### Emulador android
`npx react-native run-android --verbose`

### Emulador android release
`npx react-native run-android --variant release`

### Problemas
Program type already present: com.reactnativecommunity.picker.BuildConfig

`npm uninstall @react-native-community/picker`


<div id='intel'/>  
## A

akjshdajkshdkjashdjashdkjahsdashdashd
