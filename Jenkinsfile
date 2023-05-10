podTemplate(containers: [
    containerTemplate(
        name: 'tdp-builder', 
        image: 'yanisbariteau/tdp-builder:jenkins', 
        command: 'sleep', 
        args: '30d'
        )
  ]) {

    node(POD_LABEL) {
        container('tdp-builder') {
            environment {
                number="${currentBuild.number}"
            }
            stage('Git Clone') {
                echo "Cloning.."
                git branch: '5.1-TDP-alliage-k8s', url: 'https://github.com/Yanis77240/phoenix'
            }   
            stage ('Build') {
                echo "Building.."
                sh '''
                mvn clean install -DskipTests -Dhbase.profile=2.1
                '''
            }
            /*stage('Test') {
                echo "Testing.."
                sh '''
                mvn test -Dhbase.profile=2.1 --fail-never
                '''
            }*/
            stage('Deliver') {
                echo "Deploy..."
                withCredentials([usernamePassword(credentialsId: '4b87bd68-ad4c-11ed-afa1-0242ac120002', passwordVariable: 'pass', usernameVariable: 'user')]) {
                    sh 'mvn clean deploy -DskipTests -Dhbase.profile=2.1 -s settings.xml'
                }
            }
            stage("Publish tar.gz to Nexus") {
                echo "Publish tar.gz..."
                withCredentials([usernamePassword(credentialsId: '4b87bd68-ad4c-11ed-afa1-0242ac120002', passwordVariable: 'pass', usernameVariable: 'user')]) {
                    sh '''
                    curl -v -u $user:$pass --upload-file phoenix-assembly/target/phoenix-hbase-2.1-5.1.3-TDP-0.1.0-SNAPSHOT-bin.tar.gz http://10.110.4.212:8081/repository/maven-tar-files/phoenix/phoenix-hbase-2.1-5.1.3-TDP-0.1.0-SNAPSHOT-bin-${number}.tar.gz
                    '''
                }
            }       
        }
    }
}