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

## Instalação em ambiente Arm

Instalar dependências
```console
$ npm install
```

Configure watchamn
```console
$ echo 999999 | sudo tee -a /proc/sys/fs/inotify/max_user_watches
```

Iniciar react
```console
$ npx react-native start
```

Emulador android
```console
$ npx react-native run-android --verbose
```

Emulador android release
```console
$ npx react-native run-android --variant release
```

Problemas
>*Program type already present: com.reactnativecommunity.picker.BuildConfig
```console
$ npm uninstall @react-native-community/picker
```
<div id='intel'/>  


## Instalação em ambiente Intel

akjshdajkshdkjashdjashdkjahsdashdashd
