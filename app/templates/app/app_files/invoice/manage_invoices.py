<div class="row">
    <div class="col-lg-12">
        <div class="card">
            <div class="card-body">
                <div class="table">
                    <table class="table-bordered" width="100%" cellspacing="0" style="color:#000000">
                        <thead>
                            <th>UID</th>
                            <th class="text-center">Contact Name</th>
                            <th class="text-center">Amount</th>
                            <th class="text-center">Payment Type</th>
                            <th class="text-center">Status</th>
                            <th class="text-center">Due Date</th>
                            <th class="text-center">Collected On Date</th>
                            <th class="text-center">Created On Date</th>               
                            <th class="text-center">Action</th>                
                        </thead>
                        <tbody>
                            {% for record in collections %}
                                <tr
                                    {% if record.collection_status == 1 %}
                                        style="background-color:#ffa50069"
                                    {% elif record.collection_status == 2 %}    
                                        style="background-color:rgba(125, 205, 241, 0.5)"
                                    {% else %}
                                        style="background-color:rgba(12, 235, 19, 0.5)"
                                    {% endif %}
                                >
                                    <td>C-0000{{record.id}}</td>
                                    <td>{{record.contact.contact_name}}</td>
                                    <td>{{record.amount|safe}}</td>
                                    <td>{{record.get_payment_type_display|upper}}</td>
                                    <td>{{record.get_collection_status_display|upper}}</td>
                                    <td>{{record.collection_due_date}}</td>
                                    <td>{{record.collection_date}}</td>
                                    <td>{{record.created_on}}</td>                      
                                    <td>
                                        <a href="" class="btn btn-primary btn-sm" title="Edit Collection">
                                            <i class="fas fas-fw fa-pencil-alt"></i>
                                        </a>                                        
                                        <a href="{% url 'add-partial-collections' record.id %}" class="btn button-orange btn-sm" title="Add Partial Collection">
                                            <i class="fas fas-fw fa-hand-holding-usd"></i>
                                        </a>
                                        {% if record.collection_status == 3 %}
                                        <a href="{% url 'create-collection-invoice' record.id %}" class="btn button-black btn-sm" title="Create Invoice">
                                            <i style="color:#FFFFFF" class="fas fas-fw fa-file-invoice"></i style="color:#FFFFFF">
                                        </a>
                                        {% endif %}
                                    </td>                 
                                </tr>
                            {% endfor %}
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </div>
</div>
