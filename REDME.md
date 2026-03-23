Cybersecurity Challenge - Malware Simulation & Defense

Este projeto foi desenvolvido como o desafio final do Bootcamp Santander & DIO - CyberSecurity. O objetivo é demonstrar, de forma prática e em ambiente controlado, o funcionamento de malwares e, crucialmente, como implementar estratégias de defesa eficazes.

    Atenção: Os scripts aqui desenvolvidos são estritamente para fins educacionais, destinados ao uso de estudantes e profissionais de Pentest em ambientes isolados.

🛠️ Ambiente de Testes

Para garantir a segurança e evitar impactos em sistemas reais, foi utilizada a seguinte infraestrutura:

    Host de Desenvolvimento: Ubuntu para criação dos scripts em Python.

    Alvo (Target): Windows 7 em Máquina Virtual.

    Isolamento: Uso de ambientes virtuais (venv) para gerenciar bibliotecas e evitar conflitos.

☣️ Malware 1: Ransomware Simulado

O script simula o sequestro de dados através de criptografia simétrica.

    Bibliotecas Utilizadas: Cryptography (módulo Fernet) e os.

    Funcionamento:

        Gera uma chave de encriptação aleatória e a armazena em um arquivo local.

        Localiza todos os arquivos em um diretório alvo específico (pasta "testes").

        Criptografa o conteúdo, tornando os dados originais ilegíveis.

        Remove os arquivos originais, deixando apenas as versões cifradas e uma mensagem de resgate.

⌨️ Malware 2: Keylogger Profissional

O script captura entradas de teclado e as envia para um servidor remoto de forma silenciosa.

    Bibliotecas Utilizadas: Pynput, Smtplib, email.mime.text e threading.

    Destaques Técnicos:

        Filtro de Captura: Ignora teclas de sistema como Alt e Shift para gerar um log limpo e útil.

        Automação de Exfiltração: Envio automático dos dados capturados via e-mail (SMTP) a cada 60 segundos.

        Persistência e Sigilo: Execução em background no Windows através da extensão .pyw.

        Gestão de Dados: Limpeza automática do log local após o envio bem-sucedido para evitar detecção.

🛡️ Estratégias de Mitigação e Defesa

A principal entrega deste projeto é a compreensão de como evitar essas ameaças no mundo real:

    Defesa em Camadas: Manter Antivírus e Firewalls sempre atualizados como primeira linha de detecção de atividades suspeitas.

    Conscientização (Security Awareness): Treinar usuários para identificar táticas de Engenharia Social, evitando cliques em anexos ou links maliciosos.

    Boas Práticas de Desenvolvimento: Executar testes e códigos desconhecidos sempre em ambientes controlados (Sandboxing/VMs).
