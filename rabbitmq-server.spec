#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x6B73A36E6026DFCA (info@rabbitmq.com)
#
Name     : rabbitmq-server
Version  : 3.7.9
Release  : 47
URL      : https://github.com/rabbitmq/rabbitmq-server/releases/download/v3.7.9/rabbitmq-server-generic-unix-3.7.9.tar.xz
Source0  : https://github.com/rabbitmq/rabbitmq-server/releases/download/v3.7.9/rabbitmq-server-generic-unix-3.7.9.tar.xz
Source1  : rabbitmq-server.service
Source2  : rabbitmq-server.tmpfiles
Source99 : https://github.com/rabbitmq/rabbitmq-server/releases/download/v3.7.9/rabbitmq-server-generic-unix-3.7.9.tar.xz.asc
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 BSD-2-Clause BSD-3-Clause MIT MPL-1.1 MPL-2.0-no-copyleft-exception
Requires: rabbitmq-server-bin = %{version}-%{release}
Requires: rabbitmq-server-config = %{version}-%{release}
Requires: rabbitmq-server-license = %{version}-%{release}
Requires: rabbitmq-server-man = %{version}-%{release}
Requires: rabbitmq-server-services = %{version}-%{release}
Requires: otp
Patch1: 0001-Add-Makefile-and-correct-defaults.patch

%description
Put your EZs here and use rabbitmq-plugins to enable them.

%package bin
Summary: bin components for the rabbitmq-server package.
Group: Binaries
Requires: rabbitmq-server-config = %{version}-%{release}
Requires: rabbitmq-server-license = %{version}-%{release}
Requires: rabbitmq-server-man = %{version}-%{release}
Requires: rabbitmq-server-services = %{version}-%{release}

%description bin
bin components for the rabbitmq-server package.


%package config
Summary: config components for the rabbitmq-server package.
Group: Default

%description config
config components for the rabbitmq-server package.


%package doc
Summary: doc components for the rabbitmq-server package.
Group: Documentation
Requires: rabbitmq-server-man = %{version}-%{release}

%description doc
doc components for the rabbitmq-server package.


%package license
Summary: license components for the rabbitmq-server package.
Group: Default

%description license
license components for the rabbitmq-server package.


%package man
Summary: man components for the rabbitmq-server package.
Group: Default

%description man
man components for the rabbitmq-server package.


%package services
Summary: services components for the rabbitmq-server package.
Group: Systemd services

%description services
services components for the rabbitmq-server package.


%prep
%setup -q -n rabbitmq_server-3.7.9
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1542347552
make

%install
export SOURCE_DATE_EPOCH=1542347552
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/rabbitmq-server
cp LICENSE %{buildroot}/usr/share/package-licenses/rabbitmq-server/LICENSE
cp LICENSE-APACHE2 %{buildroot}/usr/share/package-licenses/rabbitmq-server/LICENSE-APACHE2
cp LICENSE-APACHE2-ExplorerCanvas %{buildroot}/usr/share/package-licenses/rabbitmq-server/LICENSE-APACHE2-ExplorerCanvas
cp LICENSE-APACHE2-excanvas %{buildroot}/usr/share/package-licenses/rabbitmq-server/LICENSE-APACHE2-excanvas
cp LICENSE-APL2-Stomp-Websocket %{buildroot}/usr/share/package-licenses/rabbitmq-server/LICENSE-APL2-Stomp-Websocket
cp LICENSE-BSD-base64js %{buildroot}/usr/share/package-licenses/rabbitmq-server/LICENSE-BSD-base64js
cp LICENSE-BSD-recon %{buildroot}/usr/share/package-licenses/rabbitmq-server/LICENSE-BSD-recon
cp LICENSE-MIT-EJS %{buildroot}/usr/share/package-licenses/rabbitmq-server/LICENSE-MIT-EJS
cp LICENSE-MIT-EJS10 %{buildroot}/usr/share/package-licenses/rabbitmq-server/LICENSE-MIT-EJS10
cp LICENSE-MIT-Erlware-Commons %{buildroot}/usr/share/package-licenses/rabbitmq-server/LICENSE-MIT-Erlware-Commons
cp LICENSE-MIT-Flot %{buildroot}/usr/share/package-licenses/rabbitmq-server/LICENSE-MIT-Flot
cp LICENSE-MIT-Mochi %{buildroot}/usr/share/package-licenses/rabbitmq-server/LICENSE-MIT-Mochi
cp LICENSE-MIT-Sammy %{buildroot}/usr/share/package-licenses/rabbitmq-server/LICENSE-MIT-Sammy
cp LICENSE-MIT-Sammy060 %{buildroot}/usr/share/package-licenses/rabbitmq-server/LICENSE-MIT-Sammy060
cp LICENSE-MIT-jQuery %{buildroot}/usr/share/package-licenses/rabbitmq-server/LICENSE-MIT-jQuery
cp LICENSE-MIT-jQuery164 %{buildroot}/usr/share/package-licenses/rabbitmq-server/LICENSE-MIT-jQuery164
cp LICENSE-MPL-RabbitMQ %{buildroot}/usr/share/package-licenses/rabbitmq-server/LICENSE-MPL-RabbitMQ
cp LICENSE-MPL2 %{buildroot}/usr/share/package-licenses/rabbitmq-server/LICENSE-MPL2
cp LICENSE-erlcloud %{buildroot}/usr/share/package-licenses/rabbitmq-server/LICENSE-erlcloud
cp LICENSE-httpc_aws %{buildroot}/usr/share/package-licenses/rabbitmq-server/LICENSE-httpc_aws
cp LICENSE-rabbitmq_aws %{buildroot}/usr/share/package-licenses/rabbitmq-server/LICENSE-rabbitmq_aws
%make_install
mkdir -p %{buildroot}/usr/lib/systemd/system
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/systemd/system/rabbitmq-server.service
mkdir -p %{buildroot}/usr/lib/tmpfiles.d
install -m 0644 %{SOURCE2} %{buildroot}/usr/lib/tmpfiles.d/rabbitmq-server.conf

%files
%defattr(-,root,root,-)
/usr/lib/rabbitmq-server/ebin/background_gc.beam
/usr/lib/rabbitmq-server/ebin/code_server_cache.beam
/usr/lib/rabbitmq-server/ebin/dtree.beam
/usr/lib/rabbitmq-server/ebin/gatherer.beam
/usr/lib/rabbitmq-server/ebin/gm.beam
/usr/lib/rabbitmq-server/ebin/lager_exchange_backend.beam
/usr/lib/rabbitmq-server/ebin/lqueue.beam
/usr/lib/rabbitmq-server/ebin/mirrored_supervisor_sups.beam
/usr/lib/rabbitmq-server/ebin/pg_local.beam
/usr/lib/rabbitmq-server/ebin/rabbit.app
/usr/lib/rabbitmq-server/ebin/rabbit.beam
/usr/lib/rabbitmq-server/ebin/rabbit_access_control.beam
/usr/lib/rabbitmq-server/ebin/rabbit_alarm.beam
/usr/lib/rabbitmq-server/ebin/rabbit_amqqueue.beam
/usr/lib/rabbitmq-server/ebin/rabbit_amqqueue_process.beam
/usr/lib/rabbitmq-server/ebin/rabbit_amqqueue_sup.beam
/usr/lib/rabbitmq-server/ebin/rabbit_amqqueue_sup_sup.beam
/usr/lib/rabbitmq-server/ebin/rabbit_auth_backend_internal.beam
/usr/lib/rabbitmq-server/ebin/rabbit_auth_mechanism_amqplain.beam
/usr/lib/rabbitmq-server/ebin/rabbit_auth_mechanism_cr_demo.beam
/usr/lib/rabbitmq-server/ebin/rabbit_auth_mechanism_plain.beam
/usr/lib/rabbitmq-server/ebin/rabbit_autoheal.beam
/usr/lib/rabbitmq-server/ebin/rabbit_basic.beam
/usr/lib/rabbitmq-server/ebin/rabbit_binding.beam
/usr/lib/rabbitmq-server/ebin/rabbit_boot_steps.beam
/usr/lib/rabbitmq-server/ebin/rabbit_channel.beam
/usr/lib/rabbitmq-server/ebin/rabbit_channel_interceptor.beam
/usr/lib/rabbitmq-server/ebin/rabbit_channel_sup.beam
/usr/lib/rabbitmq-server/ebin/rabbit_channel_sup_sup.beam
/usr/lib/rabbitmq-server/ebin/rabbit_client_sup.beam
/usr/lib/rabbitmq-server/ebin/rabbit_config.beam
/usr/lib/rabbitmq-server/ebin/rabbit_connection_helper_sup.beam
/usr/lib/rabbitmq-server/ebin/rabbit_connection_sup.beam
/usr/lib/rabbitmq-server/ebin/rabbit_connection_tracking.beam
/usr/lib/rabbitmq-server/ebin/rabbit_connection_tracking_handler.beam
/usr/lib/rabbitmq-server/ebin/rabbit_control_pbe.beam
/usr/lib/rabbitmq-server/ebin/rabbit_core_metrics_gc.beam
/usr/lib/rabbitmq-server/ebin/rabbit_credential_validation.beam
/usr/lib/rabbitmq-server/ebin/rabbit_credential_validator.beam
/usr/lib/rabbitmq-server/ebin/rabbit_credential_validator_accept_everything.beam
/usr/lib/rabbitmq-server/ebin/rabbit_credential_validator_min_password_length.beam
/usr/lib/rabbitmq-server/ebin/rabbit_credential_validator_password_regexp.beam
/usr/lib/rabbitmq-server/ebin/rabbit_dead_letter.beam
/usr/lib/rabbitmq-server/ebin/rabbit_diagnostics.beam
/usr/lib/rabbitmq-server/ebin/rabbit_direct.beam
/usr/lib/rabbitmq-server/ebin/rabbit_disk_monitor.beam
/usr/lib/rabbitmq-server/ebin/rabbit_epmd_monitor.beam
/usr/lib/rabbitmq-server/ebin/rabbit_exchange.beam
/usr/lib/rabbitmq-server/ebin/rabbit_exchange_decorator.beam
/usr/lib/rabbitmq-server/ebin/rabbit_exchange_parameters.beam
/usr/lib/rabbitmq-server/ebin/rabbit_exchange_type_direct.beam
/usr/lib/rabbitmq-server/ebin/rabbit_exchange_type_fanout.beam
/usr/lib/rabbitmq-server/ebin/rabbit_exchange_type_headers.beam
/usr/lib/rabbitmq-server/ebin/rabbit_exchange_type_invalid.beam
/usr/lib/rabbitmq-server/ebin/rabbit_exchange_type_topic.beam
/usr/lib/rabbitmq-server/ebin/rabbit_fhc_helpers.beam
/usr/lib/rabbitmq-server/ebin/rabbit_file.beam
/usr/lib/rabbitmq-server/ebin/rabbit_framing.beam
/usr/lib/rabbitmq-server/ebin/rabbit_guid.beam
/usr/lib/rabbitmq-server/ebin/rabbit_health_check.beam
/usr/lib/rabbitmq-server/ebin/rabbit_hipe.beam
/usr/lib/rabbitmq-server/ebin/rabbit_lager.beam
/usr/lib/rabbitmq-server/ebin/rabbit_limiter.beam
/usr/lib/rabbitmq-server/ebin/rabbit_looking_glass.beam
/usr/lib/rabbitmq-server/ebin/rabbit_memory_monitor.beam
/usr/lib/rabbitmq-server/ebin/rabbit_metrics.beam
/usr/lib/rabbitmq-server/ebin/rabbit_mirror_queue_coordinator.beam
/usr/lib/rabbitmq-server/ebin/rabbit_mirror_queue_master.beam
/usr/lib/rabbitmq-server/ebin/rabbit_mirror_queue_misc.beam
/usr/lib/rabbitmq-server/ebin/rabbit_mirror_queue_mode.beam
/usr/lib/rabbitmq-server/ebin/rabbit_mirror_queue_mode_all.beam
/usr/lib/rabbitmq-server/ebin/rabbit_mirror_queue_mode_exactly.beam
/usr/lib/rabbitmq-server/ebin/rabbit_mirror_queue_mode_nodes.beam
/usr/lib/rabbitmq-server/ebin/rabbit_mirror_queue_slave.beam
/usr/lib/rabbitmq-server/ebin/rabbit_mirror_queue_sync.beam
/usr/lib/rabbitmq-server/ebin/rabbit_mnesia.beam
/usr/lib/rabbitmq-server/ebin/rabbit_mnesia_rename.beam
/usr/lib/rabbitmq-server/ebin/rabbit_msg_file.beam
/usr/lib/rabbitmq-server/ebin/rabbit_msg_store.beam
/usr/lib/rabbitmq-server/ebin/rabbit_msg_store_ets_index.beam
/usr/lib/rabbitmq-server/ebin/rabbit_msg_store_gc.beam
/usr/lib/rabbitmq-server/ebin/rabbit_networking.beam
/usr/lib/rabbitmq-server/ebin/rabbit_node_monitor.beam
/usr/lib/rabbitmq-server/ebin/rabbit_nodes.beam
/usr/lib/rabbitmq-server/ebin/rabbit_parameter_validation.beam
/usr/lib/rabbitmq-server/ebin/rabbit_password.beam
/usr/lib/rabbitmq-server/ebin/rabbit_password_hashing_md5.beam
/usr/lib/rabbitmq-server/ebin/rabbit_password_hashing_sha256.beam
/usr/lib/rabbitmq-server/ebin/rabbit_password_hashing_sha512.beam
/usr/lib/rabbitmq-server/ebin/rabbit_peer_discovery.beam
/usr/lib/rabbitmq-server/ebin/rabbit_peer_discovery_classic_config.beam
/usr/lib/rabbitmq-server/ebin/rabbit_peer_discovery_dns.beam
/usr/lib/rabbitmq-server/ebin/rabbit_plugins.beam
/usr/lib/rabbitmq-server/ebin/rabbit_policies.beam
/usr/lib/rabbitmq-server/ebin/rabbit_policy.beam
/usr/lib/rabbitmq-server/ebin/rabbit_policy_merge_strategy.beam
/usr/lib/rabbitmq-server/ebin/rabbit_prelaunch.beam
/usr/lib/rabbitmq-server/ebin/rabbit_prequeue.beam
/usr/lib/rabbitmq-server/ebin/rabbit_priority_queue.beam
/usr/lib/rabbitmq-server/ebin/rabbit_queue_collector.beam
/usr/lib/rabbitmq-server/ebin/rabbit_queue_consumers.beam
/usr/lib/rabbitmq-server/ebin/rabbit_queue_decorator.beam
/usr/lib/rabbitmq-server/ebin/rabbit_queue_index.beam
/usr/lib/rabbitmq-server/ebin/rabbit_queue_location_client_local.beam
/usr/lib/rabbitmq-server/ebin/rabbit_queue_location_min_masters.beam
/usr/lib/rabbitmq-server/ebin/rabbit_queue_location_random.beam
/usr/lib/rabbitmq-server/ebin/rabbit_queue_location_validator.beam
/usr/lib/rabbitmq-server/ebin/rabbit_queue_master_location_misc.beam
/usr/lib/rabbitmq-server/ebin/rabbit_reader.beam
/usr/lib/rabbitmq-server/ebin/rabbit_recovery_terms.beam
/usr/lib/rabbitmq-server/ebin/rabbit_restartable_sup.beam
/usr/lib/rabbitmq-server/ebin/rabbit_router.beam
/usr/lib/rabbitmq-server/ebin/rabbit_runtime_parameters.beam
/usr/lib/rabbitmq-server/ebin/rabbit_ssl.beam
/usr/lib/rabbitmq-server/ebin/rabbit_sup.beam
/usr/lib/rabbitmq-server/ebin/rabbit_table.beam
/usr/lib/rabbitmq-server/ebin/rabbit_trace.beam
/usr/lib/rabbitmq-server/ebin/rabbit_upgrade.beam
/usr/lib/rabbitmq-server/ebin/rabbit_upgrade_functions.beam
/usr/lib/rabbitmq-server/ebin/rabbit_variable_queue.beam
/usr/lib/rabbitmq-server/ebin/rabbit_version.beam
/usr/lib/rabbitmq-server/ebin/rabbit_vhost.beam
/usr/lib/rabbitmq-server/ebin/rabbit_vhost_limit.beam
/usr/lib/rabbitmq-server/ebin/rabbit_vhost_msg_store.beam
/usr/lib/rabbitmq-server/ebin/rabbit_vhost_process.beam
/usr/lib/rabbitmq-server/ebin/rabbit_vhost_sup.beam
/usr/lib/rabbitmq-server/ebin/rabbit_vhost_sup_sup.beam
/usr/lib/rabbitmq-server/ebin/rabbit_vhost_sup_wrapper.beam
/usr/lib/rabbitmq-server/ebin/rabbit_vm.beam
/usr/lib/rabbitmq-server/ebin/supervised_lifecycle.beam
/usr/lib/rabbitmq-server/ebin/tcp_listener.beam
/usr/lib/rabbitmq-server/ebin/tcp_listener_sup.beam
/usr/lib/rabbitmq-server/ebin/term_to_binary_compat.beam
/usr/lib/rabbitmq-server/ebin/truncate.beam
/usr/lib/rabbitmq-server/escript/rabbitmq-diagnostics
/usr/lib/rabbitmq-server/escript/rabbitmq-plugins
/usr/lib/rabbitmq-server/escript/rabbitmqctl
/usr/lib/rabbitmq-server/include/gm_specs.hrl
/usr/lib/rabbitmq-server/include/rabbit.hrl
/usr/lib/rabbitmq-server/include/rabbit_core_metrics.hrl
/usr/lib/rabbitmq-server/include/rabbit_framing.hrl
/usr/lib/rabbitmq-server/include/rabbit_log.hrl
/usr/lib/rabbitmq-server/include/rabbit_memory.hrl
/usr/lib/rabbitmq-server/include/rabbit_misc.hrl
/usr/lib/rabbitmq-server/include/rabbit_msg_store.hrl
/usr/lib/rabbitmq-server/plugins/README
/usr/lib/rabbitmq-server/plugins/amqp10_client-3.7.9.ez
/usr/lib/rabbitmq-server/plugins/amqp10_common-3.7.9.ez
/usr/lib/rabbitmq-server/plugins/amqp_client-3.7.9.ez
/usr/lib/rabbitmq-server/plugins/cowboy-2.4.0.ez
/usr/lib/rabbitmq-server/plugins/cowlib-2.3.0.ez
/usr/lib/rabbitmq-server/plugins/goldrush-0.1.9.ez
/usr/lib/rabbitmq-server/plugins/jsx-2.9.0.ez
/usr/lib/rabbitmq-server/plugins/lager-3.6.5.ez
/usr/lib/rabbitmq-server/plugins/rabbit_common-3.7.9.ez
/usr/lib/rabbitmq-server/plugins/rabbitmq_amqp1_0-3.7.9.ez
/usr/lib/rabbitmq-server/plugins/rabbitmq_auth_backend_cache-3.7.9.ez
/usr/lib/rabbitmq-server/plugins/rabbitmq_auth_backend_http-3.7.9.ez
/usr/lib/rabbitmq-server/plugins/rabbitmq_auth_backend_ldap-3.7.9.ez
/usr/lib/rabbitmq-server/plugins/rabbitmq_auth_mechanism_ssl-3.7.9.ez
/usr/lib/rabbitmq-server/plugins/rabbitmq_aws-3.7.9.ez
/usr/lib/rabbitmq-server/plugins/rabbitmq_consistent_hash_exchange-3.7.9.ez
/usr/lib/rabbitmq-server/plugins/rabbitmq_event_exchange-3.7.9.ez
/usr/lib/rabbitmq-server/plugins/rabbitmq_federation-3.7.9.ez
/usr/lib/rabbitmq-server/plugins/rabbitmq_federation_management-3.7.9.ez
/usr/lib/rabbitmq-server/plugins/rabbitmq_jms_topic_exchange-3.7.9.ez
/usr/lib/rabbitmq-server/plugins/rabbitmq_management-3.7.9.ez
/usr/lib/rabbitmq-server/plugins/rabbitmq_management_agent-3.7.9.ez
/usr/lib/rabbitmq-server/plugins/rabbitmq_mqtt-3.7.9.ez
/usr/lib/rabbitmq-server/plugins/rabbitmq_peer_discovery_aws-3.7.9.ez
/usr/lib/rabbitmq-server/plugins/rabbitmq_peer_discovery_common-3.7.9.ez
/usr/lib/rabbitmq-server/plugins/rabbitmq_peer_discovery_consul-3.7.9.ez
/usr/lib/rabbitmq-server/plugins/rabbitmq_peer_discovery_etcd-3.7.9.ez
/usr/lib/rabbitmq-server/plugins/rabbitmq_peer_discovery_k8s-3.7.9.ez
/usr/lib/rabbitmq-server/plugins/rabbitmq_random_exchange-3.7.9.ez
/usr/lib/rabbitmq-server/plugins/rabbitmq_recent_history_exchange-3.7.9.ez
/usr/lib/rabbitmq-server/plugins/rabbitmq_sharding-3.7.9.ez
/usr/lib/rabbitmq-server/plugins/rabbitmq_shovel-3.7.9.ez
/usr/lib/rabbitmq-server/plugins/rabbitmq_shovel_management-3.7.9.ez
/usr/lib/rabbitmq-server/plugins/rabbitmq_stomp-3.7.9.ez
/usr/lib/rabbitmq-server/plugins/rabbitmq_top-3.7.9.ez
/usr/lib/rabbitmq-server/plugins/rabbitmq_tracing-3.7.9.ez
/usr/lib/rabbitmq-server/plugins/rabbitmq_trust_store-3.7.9.ez
/usr/lib/rabbitmq-server/plugins/rabbitmq_web_dispatch-3.7.9.ez
/usr/lib/rabbitmq-server/plugins/rabbitmq_web_mqtt-3.7.9.ez
/usr/lib/rabbitmq-server/plugins/rabbitmq_web_mqtt_examples-3.7.9.ez
/usr/lib/rabbitmq-server/plugins/rabbitmq_web_stomp-3.7.9.ez
/usr/lib/rabbitmq-server/plugins/rabbitmq_web_stomp_examples-3.7.9.ez
/usr/lib/rabbitmq-server/plugins/ranch-1.6.2.ez
/usr/lib/rabbitmq-server/plugins/ranch_proxy_protocol-2.1.1.ez
/usr/lib/rabbitmq-server/plugins/recon-2.3.6.ez
/usr/lib/rabbitmq-server/plugins/syslog-3.4.5.ez
/usr/lib/rabbitmq-server/priv/schema/rabbit.schema
/usr/lib/rabbitmq-server/sbin/cuttlefish
/usr/lib/rabbitmq-server/sbin/rabbitmq-defaults
/usr/lib/rabbitmq-server/sbin/rabbitmq-diagnostics
/usr/lib/rabbitmq-server/sbin/rabbitmq-env
/usr/lib/rabbitmq-server/sbin/rabbitmq-env.orig
/usr/lib/rabbitmq-server/sbin/rabbitmq-plugins
/usr/lib/rabbitmq-server/sbin/rabbitmq-server
/usr/lib/rabbitmq-server/sbin/rabbitmqctl

%files bin
%defattr(-,root,root,-)
%exclude /usr/bin/cuttlefish
/usr/bin/rabbitmq-defaults
/usr/bin/rabbitmq-diagnostics
/usr/bin/rabbitmq-env
/usr/bin/rabbitmq-plugins
/usr/bin/rabbitmq-server
/usr/bin/rabbitmqctl

%files config
%defattr(-,root,root,-)
/usr/lib/tmpfiles.d/rabbitmq-server.conf

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/rabbitmq\-server/*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/rabbitmq-server/LICENSE
/usr/share/package-licenses/rabbitmq-server/LICENSE-APACHE2
/usr/share/package-licenses/rabbitmq-server/LICENSE-APACHE2-ExplorerCanvas
/usr/share/package-licenses/rabbitmq-server/LICENSE-APACHE2-excanvas
/usr/share/package-licenses/rabbitmq-server/LICENSE-APL2-Stomp-Websocket
/usr/share/package-licenses/rabbitmq-server/LICENSE-BSD-base64js
/usr/share/package-licenses/rabbitmq-server/LICENSE-BSD-recon
/usr/share/package-licenses/rabbitmq-server/LICENSE-MIT-EJS
/usr/share/package-licenses/rabbitmq-server/LICENSE-MIT-EJS10
/usr/share/package-licenses/rabbitmq-server/LICENSE-MIT-Erlware-Commons
/usr/share/package-licenses/rabbitmq-server/LICENSE-MIT-Flot
/usr/share/package-licenses/rabbitmq-server/LICENSE-MIT-Mochi
/usr/share/package-licenses/rabbitmq-server/LICENSE-MIT-Sammy
/usr/share/package-licenses/rabbitmq-server/LICENSE-MIT-Sammy060
/usr/share/package-licenses/rabbitmq-server/LICENSE-MIT-jQuery
/usr/share/package-licenses/rabbitmq-server/LICENSE-MIT-jQuery164
/usr/share/package-licenses/rabbitmq-server/LICENSE-MPL-RabbitMQ
/usr/share/package-licenses/rabbitmq-server/LICENSE-MPL2
/usr/share/package-licenses/rabbitmq-server/LICENSE-erlcloud
/usr/share/package-licenses/rabbitmq-server/LICENSE-httpc_aws
/usr/share/package-licenses/rabbitmq-server/LICENSE-rabbitmq_aws

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man5/rabbitmq-env.conf.5.gz
/usr/share/man/man8/rabbitmq-echopid.8.gz
/usr/share/man/man8/rabbitmq-plugins.8.gz
/usr/share/man/man8/rabbitmq-server.8.gz
/usr/share/man/man8/rabbitmq-service.8.gz
/usr/share/man/man8/rabbitmqctl.8.gz

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/rabbitmq-server.service
